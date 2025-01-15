from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.StockListView.as_view(), name='inventory'),
    path('new', views.StockCreateView.as_view(), name='new-stock'),
    path('stock/<pk>/edit', views.StockUpdateView.as_view(), name='edit-stock'),
    path('stock/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),

    path('product',views.product, name='product'),
    path('p_form',views.p_form, name='p_form'),
    path('editP/<product_p_id>', views.p_edit, name='editP'),
    path('deleteP/<product_p_id>',views.p_delete),

    path('employee',views.employee,name='employee'),
    path('dependent',views.dependent,name='dependent'),
    path('em_form',views.em_form,name='em_form'),
    path('edit/<employee_em_id>',views.em_edit),
    path('delete/<employee_em_id>',views.em_delete),
    #path('dep/<employee_em_id>', views.em_dep, name='dep'),

    path('customer',views.customer,name='customer'),
    path('c_form',views.c_form,name='c_form'),
    path('editC/<customer_c_id>',views.c_edit),
    path('deleteC/<customer_c_id>',views.c_delete),

    path('create_receipt/', views.create_receipt, name='create_receipt'),
    path('list_receipts/', views.list_receipts, name='list_receipts'),
    path('list_receipts/deleteR/<int:receipt_id>/', views.receipt_delete, name='deleteR'),
    

    path('report/', views.report, name='report'),
    path('reportdate/', views.reportdate, name='reportdate'),
    path('reportcat/', views.reportcat, name='reportcat'),
    path('reporttype/', views.reporttype, name='reporttype'),
    path('daily_report/', views.daily_report, name='daily_report'),

    #path('receipt/', views.receipt, name='receipt'),
    path('list_receipts/receipt/<int:receipt_id>/', views.receipt, name='receipt'),
    path('reportcus/', views.reportcus, name='reportcus'),
    path('customer-list/', views.customer_list, name='customer_list'),


 
]