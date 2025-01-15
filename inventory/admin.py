from django.contrib import admin
from .models import Stock
from .models import Employee
from .models import Dependent
from .models import Customer
from .models import Product
from .models import Category
from .models import Category1
from .models import Receipt
#from .models import ReceiptProduct


admin.site.register(Stock)
admin.site.register(Employee)
admin.site.register(Dependent)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Category1)
admin.site.register(Receipt)
#admin.site.register(ReceiptProduct)