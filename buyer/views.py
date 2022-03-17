from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum


from buyer.forms import BuyerForm, BuyerEntryForm
from buyer.models import Buyer, BuyerEntry
from dashboard.models import Product

@login_required
def buyers_view(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            buyer = form.save(commit=False)
            buyer.save()
            messages.success(request, 'Buyer saved with success!')
            return redirect('buyer:buyers')
    else:
        form = BuyerForm()

    buyers = Buyer.objects.all()
    return render(request,"buyer/buyers.html", {'form': form, 'buyers':buyers })


@login_required
def entry_view(request):
    if request.method == 'POST':
        form = BuyerEntryForm(request.POST, request.FILES)
        if form.is_valid():
            buyerentry = form.save(commit=False)
            buyerentry.save()
            messages.success(request, 'Buyer Entry saved with success!')
            return redirect('buyer:entry')
    else:
        form = BuyerEntryForm()

    buyerentries = BuyerEntry.objects.all()

    return render(request,"buyer/entry.html", {'form': form, 'buyerentries':buyerentries })

@login_required
def entrylist_view(request):
    context = {
        'products':Product.objects.all(),
        'buyers':Buyer.objects.all(),
    }
    att_product = request.GET.get('product','')
    att_buyer = request.GET.get('buyer','')
    att_date = request.GET.get('date','')
    qs = BuyerEntry.objects.order_by('-date_of_entered')
    if att_product:
        context['att_product'] = int(att_product)
        qs=qs.filter(product_id=att_product)
    
    if att_buyer:
        context['att_buyer'] = int(att_buyer)
        qs=qs.filter(buyer_id=att_buyer)
    
    # if att_date:
    #     context['att_date'] = att_date
    context['results'] = qs
    context['total'] = qs.aggregate(c=Sum('unit_price'))['c']
    return render(request,"buyer/entrylist.html",context)