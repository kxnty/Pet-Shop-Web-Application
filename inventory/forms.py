from django import forms
from .models import Stock
from .models import Product
from .models import Customer
from .models import Receipt
from .models import ReceiptProduct


class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

    class Meta:
        model = Stock
        fields = ['name', 'quantity']



# Update your ReceiptForm to include widgets and validation
class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        exclude = ['total_amount', 'tprice']

from django import forms
from django.forms import inlineformset_factory
from .models import Receipt

#ReceiptFormSet = inlineformset_factory(
 #   Customer,  # Assuming Customer is your related model
  #  Receipt,
   # fields=['product', 'quantity', 'payment_method', 'date'],
    #extra=1  # Number of empty forms to display
#)

class ReceiptProductForm(forms.ModelForm):
    class Meta:
        model = ReceiptProduct
        fields = ['product', 'quantity']




