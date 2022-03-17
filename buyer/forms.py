from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from buyer.models import Buyer, BuyerEntry
class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__' #('name', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
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
            Submit('submit', 'Add New Buyer')
        )


UNITTYPES = (
    ('', 'Choose...'),
    ('kg', 'Kgs'),
    ('bag', 'Bags'),
    ('katta', 'Katta')
)
PAYMENTMODES = (
    ('', 'Choose...'),
    ('cash', 'Cash'),
    ('credit', 'Credit'),
    ('upi', 'UPI')
)
class BuyerEntryForm(forms.ModelForm):
    unit_type = forms.ChoiceField(choices=UNITTYPES)
    payment_mode = forms.ChoiceField(choices=PAYMENTMODES)
    class Meta:
        model = BuyerEntry
        fields = '__all__' #('name', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('buyer', css_class='form-group col-md-6 mb-0'),
                Column('product', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('unit_type', css_class='form-group col-md-3 mb-0'),
                Column('unit_price', css_class='form-group col-md-3 mb-0'),
                Column('payment_mode', css_class='form-group col-md-3 mb-0'),
                Column('labour_commn', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Add New Buyer Entry')
        )