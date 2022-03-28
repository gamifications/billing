from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Max, F
from django.views.generic.edit import UpdateView
from django.template.loader import render_to_string

import json



from buyer.pdf import GeneratePDF
from buyer.forms import BuyerForm, BuyerEntryForm
from buyer.models import Buyer, BuyerEntry, BuyerEntryItems

@login_required
def buyers_view(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            buyer = form.save(commit=False)
            buyer.save()
            messages.success(request, 'Buyer saved with success!')
            return redirect('buyer:entry')

class BuyerUpdateView(UpdateView):
    model = Buyer
    form_class = BuyerForm
    template_name_suffix = '_update_form'
from django.middleware import csrf
def buyer_update_view(request,pk):
    item= Buyer.objects.get(id=pk)
    if request.method =='POST':
        form = BuyerForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Buyer saved with success!')
            return redirect('buyer:entry')
    form = BuyerForm(instance=item)

    return HttpResponse(
        render_to_string('buyer/buyer_update_form.html', 
        {'form':form,'buyerid':pk,'csrf_token': csrf.get_token(request)}))
    

def generate_pdf(entry, req):
    pdf_gen = GeneratePDF(req.build_absolute_uri('/')[:-1]) # request.get_host()
    pdf_gen.generate(entry,BuyerEntryItems.objects.filter(buyer_entry=entry))
    return pdf_gen.url

@login_required
def entry_view(request):
    
    if request.method == 'POST':
        billno = BuyerEntry.objects.aggregate(n=Max('billnumber'))['n'] or 10000
        entry=BuyerEntry.objects.create(
            billnumber= billno+1,
            buyer_id=request.POST['buyerid'],
            payment_mode=request.POST['paymentmode']
        )
        items = json.loads(request.POST['items'])
        for item in items:
            BuyerEntryItems.objects.create(
                buyer_entry=entry,
                labour_commn=item['labour'],
                product_id=item['productid'],
                unit_type=item['unittype'],
                unit_price=item['unitprice'],
            )
        
        
        messages.success(request, 'Entry saved with success!')
        pdf_url = generate_pdf(entry,request)
        return HttpResponse(pdf_url)
    return render(request,"buyer/entry.html", {'form': BuyerEntryForm(), 'buyers':Buyer.objects.all(), 'buyer_form': BuyerForm()})

def ajax_pdf(request):
    entry=BuyerEntry.objects.get(id=request.GET['entry'])
    pdf_url = generate_pdf(entry,request)
    return HttpResponse(pdf_url)

@login_required
def entrylist_view(request):
    qs = BuyerEntry.objects.annotate(total=Sum(F('buyerentryitems__unit_price')+F('buyerentryitems__labour_commn')))
    return render(request,"buyer/entrylist.html",{'results':qs})