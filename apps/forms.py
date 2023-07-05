from django import forms
from .models import Requisition ,Issue, StoreBalance, Purchase, Transaction, ProductList
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'user_type')



class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = '__all__'



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
