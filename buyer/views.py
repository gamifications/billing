

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Max


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
    # else:
    #     form = BuyerForm()

    # buyers = Buyer.objects.all()
    # return render(request,"buyer/buyers.html", {'form': form, 'buyers':buyers })


@login_required
def entry_view(request):
    import json
    if request.method == 'POST':
        billno = BuyerEntry.objects.aggregate(n=Max('billnumber'))['n'] or 10000
        entry=BuyerEntry.objects.create(
            billnumber= billno+1,
            buyer_id=request.POST['buyerid'],
            payment_mode=request.POST['paymentmode']
        )
        for item in json.loads(request.POST['items']):
            BuyerEntryItems.objects.create(
                buyer_entry=entry,
                labour_commn=item['labour'],
                product_id=item['productid'],
                unit_type=item['unittype'],
                unit_price=item['unitprice'],
            )
        
        messages.success(request, 'Entry saved with success!')
        return HttpResponse('success')
    return render(request,"buyer/entry.html", {'form': BuyerEntryForm(), 'buyers':Buyer.objects.all(), 'buyer_form': BuyerForm()})

@login_required
def entrylist_view(request):
    qs = BuyerEntry.objects.all()
    return render(request,"buyer/entrylist.html",{'results':qs.annotate(total=Sum('buyerentryitems__unit_price'))})