
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum


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
    if request.method == 'POST':
        entry=BuyerEntry.objects.create(buyer_id=request.POST['buyerid'],payment_mode=request.POST['paymentmode'])
        for item in request.POST.getlist('items'):
            BuyerEntryItems.objects.create(
                buyer_entry=entry,
                labour_commn=item['labour_commn'],
                product=item['product'],
                unit_type=item['unit_type'],
                unit_price=item['unit_price'],
            )
        return HttpResponse('success')
    return render(request,"buyer/entry.html", {'form': BuyerEntryForm(), 'buyers':Buyer.objects.all(), 'buyer_form': BuyerForm()})

@login_required
def entrylist_view(request):
    qs = BuyerEntry.objects.order_by('-date_of_entered')
    return render(request,"buyer/entrylist.html",{'results':qs.annotate(total=Sum('buyerentryitems__unit_price'))})