from django.shortcuts import render, redirect
from .forms import RequisitionForm, IssueForm, StoreBalanceForm, PurchaseForm, TransactionForm, ProductListForm
from .models import Requisition,  Issue, StoreBalance, Purchase, Transaction, ProductList,Workorder
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Requisition

def home_page(request):
    return render(request, 'homepage.html')

def create_requisition(request):
    if request.method == 'POST':
        form = RequisitionForm(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.approval_status = 'PENDING'
            requisition.save()
            return redirect('create_requisition')
    else:
        form = RequisitionForm()
    return render(request, 'create_requisition.html', {'form': form})

def department_head(request):
    # Retrieve the requisitions from the database
    requisitions = Requisition.objects.all()
    return render(request, 'department_head.html', {'requisitions': requisitions})



def update_approval_status(request):
    if request.method == 'POST':
        requisition_no = request.POST.get('requisition_no')
        approval_status = request.POST.get('approval_status')
        approval_role = request.POST.get('approval_role')
        remarks = request.POST.get('remarks')
        # Retrieve the requisition from the database
        try:
            requisition = Requisition.objects.get(requisition_no=requisition_no)
        except Requisition.DoesNotExist:
            return JsonResponse({'error': 'Requisition not found'}, status=404)

        # Update the approval status
        requisition.approval_status = approval_status
        requisition.approval_role = approval_role
        requisition.remark = remarks
        requisition.save()

        # Return a success response
        return JsonResponse({'message': 'Approval status updated successfully'})

    # Redirect to the department_head view if accessed directly
    return redirect('department_head')

def workorder_list(request):
    workorders = Workorder.objects.all()
    return render(request, 'workorder_list.html', {'workorders': workorders})




def create_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('create_issue')
    else:
        form = IssueForm()
    return render(request, 'create_issue.html', {'form': form})

def create_store_balance(request):
    if request.method == 'POST':
        form = StoreBalanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store_balance_list')
    else:
        form = StoreBalanceForm()
    return render(request, 'create_store_balance.html', {'form': form})

def create_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')
    else:
        form = PurchaseForm()
    return render(request, 'create_purchase.html', {'form': form})

def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'create_transaction.html', {'form': form})

def create_product_list(request):
    if request.method == 'POST':
        form = ProductListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list_list')
    else:
        form = ProductListForm()
    return render(request, 'create_product_list.html', {'form': form})

def requisition_list(request):
    requisitions = Requisition.objects.all()
    print(requisitions)
    return render(request, 'requisition_list.html', {'requisitions': requisitions})


def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'issue_list.html', {'issues': issues})

def store_balance_list(request):
    store_balances = StoreBalance.objects.all()
    return render(request, 'store_balance_list.html', {'store_balances': store_balances})

def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchase_list.html', {'purchases': purchases})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

def product_list_list(request):
    product_lists = ProductList.objects.all()
    return render(request, 'product_list_list.html', {'product_lists': product_lists})
