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
        exclude = ['approval_role', 'approval_status']
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
from django import forms
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    user_type = forms.ChoiceField(choices=[('ADMINISTRATION', 'Administration'),
        ('DEPARTMENT_HEAD', 'Department Head'),
        ('STORE_EXECUTIVE', 'Store Executive'),
        ('NORMAL_USER', 'Normal User'),])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['user_type'].widget.attrs.update({'placeholder': 'User Type'})

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        # Additional validation or processing logic for user_type if needed
        return cleaned_data

