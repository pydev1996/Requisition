from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('requisition/create/', views.create_requisition, name='create_requisition'),
    path('issue/create/', views.create_issue, name='create_issue'),
    path('store_balance/create/', views.create_store_balance, name='create_store_balance'),
    path('purchase/create/', views.create_purchase, name='create_purchase'),
    path('transaction/create/', views.create_transaction, name='create_transaction'),
    path('product_list/create/', views.create_product_list, name='create_product_list'),
    path('requisition/list/', views.requisition_list, name='requisition_list'),
     path('department_head/', views.department_head, name='department_head'),
    path('store_executive/',views.store_executive,name='store_executive'),
    path('administrations/',views.administrations,name='administrations'),
    path('issue/list/', views.issue_list, name='issue_list'),
    path('store_balance/list/', views.store_balance_list, name='store_balance_list'),
    path('purchase/list/', views.purchase_list, name='purchase_list'),
    path('transaction/list/', views.transaction_list, name='transaction_list'),
    path('product_list/list/', views.product_list_list, name='product_list_list'),
    path('workorder/list/', views.workorder_list, name='workorder_list'),
    path('update_approval_status/', views.update_approval_status, name='update_approval_status'),
    path('update_approval_status2/', views.update_approval_status2, name='update_approval_status2'),
    path('update_approval_status3/', views.update_approval_status3, name='update_approval_status3'),
    path('report/<int:requisition_no>/', views.report_view, name='report'),
    path('requisition/<int:requisition_no>/add_report/', views.add_report, name='add_report'),


]
