from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Max, F
import json



from seller.pdf import GeneratePDF
from seller.forms import SellerForm, SellerEntryForm
from seller.models import Seller, SellerEntry, SellerEntryItems

@login_required
def sellers_view(request):
    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.save()
            messages.success(request, 'Seller saved with success!')
            return redirect('seller:entry')

def generate_pdf(entry, req):
    pdf_gen = GeneratePDF(req.build_absolute_uri('/')[:-1]) # request.get_host()
    pdf_gen.generate(entry,SellerEntryItems.objects.filter(seller_entry=entry))
    return pdf_gen.url

@login_required
def entry_view(request):
    
    if request.method == 'POST':
        billno = SellerEntry.objects.aggregate(n=Max('billnumber'))['n'] or 10000
        entry=SellerEntry.objects.create(
            billnumber= billno+1,
            seller_id=request.POST['sellerid'],
            payment_mode=request.POST['paymentmode']
        )
        items = json.loads(request.POST['items'])
        for item in items:
            SellerEntryItems.objects.create(
                seller_entry=entry,
                labour_commn=item['labour'],
                product_id=item['productid'],
                unit_type=item['unittype'],
                unit_price=item['unitprice'],
            )
        
        
        messages.success(request, 'Entry saved with success!')
        pdf_url = generate_pdf(entry,request)
        return HttpResponse(pdf_url)
    return render(request,"seller/entry.html", {'form': SellerEntryForm(), 'sellers':Seller.objects.all(), 'seller_form': SellerForm()})

def ajax_pdf(request):
    entry=SellerEntry.objects.get(id=request.GET['entry'])
    pdf_url = generate_pdf(entry,request)
    return HttpResponse(pdf_url)

@login_required
def entrylist_view(request):
    qs = SellerEntry.objects.annotate(total=Sum(F('sellerentryitems__unit_price')+F('sellerentryitems__labour_commn')))
    return render(request,"seller/entrylist.html",{'results':qs})