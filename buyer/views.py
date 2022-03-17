from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count


from buyer.forms import BuyerForm
from buyer.models import Buyer

@login_required
def buyers_view(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            buyer = form.save(commit=False)
            # buyer.school = request.user.school
            buyer.save()
            messages.success(request, 'Buyer saved with success!')
            return redirect('buyer:buyers')
    else:
        # buyer = Buyer(school = request.user.school)
        form = BuyerForm()

    buyers = Buyer.objects.all()
    return render(request,"buyer/buyers.html", {'form': form, 'buyers':buyers })


@login_required
def entry_view(request):
    return render(request,"buyer/entry.html")

@login_required
def entrylist_view(request):
    return render(request,"buyer/entrylist.html")