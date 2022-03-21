from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import CreateView
from django.db.models import Count
from .forms import SignUpForm, ProductForm
from .models import Product

User = get_user_model()

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup_form.html'


    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')

@login_required
def home(request):
    if request.user.is_authenticated:
        return redirect('buyer:entry')
    return render(request, 'home.html')


@login_required
def products_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            messages.success(request, 'Product saved with success!')
            return redirect('dashboard:products')
    else:
        form = ProductForm()

    products = Product.objects.annotate(stock=Count('buyerentryitems'))
    return render(request,"dashboard/products.html", {'form': form, 'products':products })

