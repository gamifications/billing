from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    CHOICES=[('buyer','Buyer'),('seller','Seller')]
    usertype = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        usertype= self.cleaned_data.get('usertype')
        if usertype == 'buyer':
            user.is_buyer = True
        else:
            user.is_seller = True
        user.save()
        return user