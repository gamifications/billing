from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from django.contrib.auth import get_user_model

from dashboard.models import Product

User = get_user_model()

class SignUpForm(UserCreationForm):
    CHOICES=[('admin','Admin'),('biller','Biller')]
    usertype = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        usertype= self.cleaned_data.get('usertype')
        if usertype == 'admin':
            user.is_staff = True
        user.save()
        return user

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__' #('name', )
    
    
