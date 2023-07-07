from django import forms
from .models import Requisition ,Issue, StoreBalance, Purchase, Transaction, ProductList
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Report

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'user_type')



class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = '__all__'
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['item_details', 'brand_name', 'unit', 'requisition_qty', 'requisition_date']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'

class StoreBalanceForm(forms.ModelForm):
    class Meta:
        model = StoreBalance
        fields = '__all__'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class ProductListForm(forms.ModelForm):
    class Meta:
        model = ProductList
        fields = '__all__'
from django import forms
from .models import Approval


class ApprovalForm(forms.ModelForm):
   

    class Meta:
        model = Approval
        fields = ['username','requisition_no', 'approval_role', 'status', 'remark']
