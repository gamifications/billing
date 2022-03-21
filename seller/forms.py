from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML

from seller.models import Seller
from dashboard.models import Product
class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__' #('name', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = '/seller/sellers/'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('father_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('mobile1', css_class='form-group col-md-4 mb-0'),
                Column('mobile2', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('district', css_class='form-group col-md-3 mb-0'),
                Column('state', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('reference_name', css_class='form-group col-md-6 mb-0'),
                Column('aadhar_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'photo',
            'email_notifications',
            'sms_notifications',
            Submit('submit', 'Add New seller')
        )


UNITTYPES = (
    ('', 'Choose...'),
    ('kg', 'Kgs'),
    ('bag', 'Bags'),
    ('katta', 'Katta')
)


class SellerEntryForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    unit_price = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Unit Price'}))
    unit_type = forms.ChoiceField(choices=UNITTYPES)
    labour_commn = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Labour charge'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('product', css_class='form-group col-md-3 mb-0'),
                Column('unit_price', css_class='form-group col-md-3 mb-0'),
                Column('unit_type', css_class='form-group col-md-3 mb-0'),
                Column('labour_commn', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Add Item')
        )