from django.shortcuts import render, redirect
from .forms import RequisitionForm, IssueForm, StoreBalanceForm, PurchaseForm, TransactionForm, ProductListForm
from .models import Requisition,  Issue, StoreBalance, Purchase, Transaction, ProductList,Workorder
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Requisition
from .models import Requisition, Report
from .forms import ReportForm

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomLoginForm

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_type = form.cleaned_data.get('user_type')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Additional logic based on user_type
                return redirect('home_page')  # Redirect to the home page or any other desired URL

    else:
        form = CustomLoginForm(request)

    return render(request, 'login.html', {'form': form})


from django.urls import reverse
def home_page(request):
    username = request.user.username
    issues = Issue.objects.filter(user_name=username,status='Approved')
    create_requisition_url = reverse('create_requisition')
    requisition_list_url = reverse('requisition_list',args=[username])
    workorder_list_url = reverse('workorder_list')
    print(issues)
    return render(request, 'homepage.html', {
        'username': username,
        'create_requisition_url': create_requisition_url,
        'requisition_list_url': requisition_list_url,
        'workorder_list_url': workorder_list_url,
        'issues': issues,
    })
def accept_issue(request, issue_id):
    issue = Issue.objects.get(issue_no=issue_id)
    issue.status = 'Accepted'
    issue.notification_status = True
    issue.save()
    return redirect('home_page')
    # ... handle the necessary operations after accepting the issue ...


def reject_issue(request, issue_id):
    issue = Issue.objects.get(issue_no=issue_id)
    issue.status = 'Rejected'
    issue.notification_status = True
    issue.save()
    return redirect('home_page')
    # ... handle the necessary operations after rejecting the issue ...

def create_requisition(request):
    if request.method == 'POST':
        form = RequisitionForm(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.approval_status = 'PENDING'
            requisition.save()
            return redirect('create_requisition')
        else:
            print(form.errors)
    else:
        form = RequisitionForm()
    return render(request, 'create_requisition.html', {'form': form})


def report_view(request, requisition_no):
    # Add your logic to retrieve the report details based on the requisition_no
    # You can pass the report details to the template or render the report page here
    report = Report.objects.filter(requisition_no=requisition_no)
    dh = Approval.objects.filter(requisition_no=requisition_no ,approval_role='Department Head')
    se = Approval.objects.filter(requisition_no=requisition_no ,approval_role='Store Executive')
    adm = Approval.objects.filter(requisition_no=requisition_no ,approval_role='Administration')
    req=Requisition.objects.get(requisition_no=requisition_no)
    return render(request, 'report.html', {'requisition_no': requisition_no,'adm':adm,"req":req,'report':report,'dh':dh,'se':se})


def add_report(request, requisition_no):
    requisition = Requisition.objects.get(requisition_no=requisition_no)
    
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.requisition_no = requisition
            report.requistion_date=requisition.requisition_date
            report.save()
            return redirect('report', requisition_no=requisition_no)
    else:
        form = ReportForm()
    
    return render(request, 'report.html', {'form': form, 'requisition': requisition, 'requisition_no': requisition_no})





from django.shortcuts import render, redirect
from .models import Approval
from .forms import ApprovalForm
def update_status(requisition_id):
    approvals = Approval.objects.filter(requisition_no=requisition_id)
    requisition = Requisition.objects.get(requisition_no=requisition_id)

    if approvals.count() == 1:
        approval = approvals.first()
        requisition.approval_status = approval.status
        requisition.remark = approval.remark
    elif approvals.count() > 1:
        # Sort approvals by id (primary key) in descending order to get the latest approval
        latest_approval = approvals.order_by('-id').first()
        requisition.approval_status = latest_approval.status
        requisition.remark = latest_approval.remark
    else:
        # Handle the case where no approval is found for the requisition
        # You can display an error message or set default values for the fields
        requisition.approval_status = 'N/A'
        requisition.remark = 'N/A'

    requisition.save()


def department_head(request):
    requisitions = Requisition.objects.all()
    form = ApprovalForm()
    return render(request, 'department_head.html', {'requisitions': requisitions, 'form': form})


def update_approval_status(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            requisition_id = request.POST.get('requisition_no')
            approval = form.save(commit=False)
            approval.requisition_no= requisition_id
            approval.save()
            update_status(requisition_id)
            return redirect('department_head')
        else:
            print(form.errors)
    else:
        form = ApprovalForm()

    requisitions = Requisition.objects.all()
    
    return render(request, 'department_head.html', {'requisitions': requisitions, 'form': form})
def store_executive(request):
    requisitions = Requisition.objects.filter(approval_status="Approved",approval_role="Department Head")
    form = ApprovalForm()
    return render(request, 'store_executive.html', {'requisitions': requisitions, 'form': form})


def update_approval_status2(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            requisition_id = request.POST.get('requisition_no')
            approval = form.save(commit=False)
            approval.requisition_no= requisition_id
            approval.save()
            update_status(requisition_id)
            return redirect('store_executive')
        else:
            print(form.errors)
    else:
        form = ApprovalForm()

    requisitions = Requisition.objects.all()
    
    return render(request, 'store_executive.html', {'requisitions': requisitions, 'form': form})

def administrations(request):
    requisitions = Requisition.objects.all()
    form = ApprovalForm()
    return render(request, 'administrations.html', {'requisitions': requisitions, 'form': form})
def workorder(requisition_id):
    approvals = Approval.objects.filter(requisition_no=requisition_id,approval_role='Administration')
    requisition = Requisition.objects.get(requisition_no=requisition_id)
    
    for approval in approvals:
        if approval.status == 'Approved':
            workorder = Workorder.objects.create(
                requisition=requisition.requisition_no,
                approval_status=requisition.approval_status,
                date=requisition.requisition_date
            )
            workorder.save()





def update_approval_status3(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            requisition_id = request.POST.get('requisition_no')
            approval = form.save(commit=False)
            approval.requisition_no= requisition_id
            approval.save()
            update_status(requisition_id)
            workorder(requisition_id)
            return redirect('administrations')
        else:
            print(form.errors)
    else:
        form = ApprovalForm()

    requisitions = Requisition.objects.all()
    
    return render(request, 'administrations.html', {'requisitions': requisitions, 'form': form})







# def update_approval_status(request):
#     if request.method == 'POST':
#         requisition_no = request.POST.get('requisition_no')
#         approval_status = request.POST.get('approval_status')
#         approval_role = request.POST.get('approval_role')
#         remarks = request.POST.get('remarks')
#         # Retrieve the requisition from the database
#         try:
#             requisition = Requisition.objects.get(requisition_no=requisition_no)
#         except Requisition.DoesNotExist:
#             return JsonResponse({'error': 'Requisition not found'}, status=404)

#         # Update the approval status
#         requisition.approval_status = approval_status
#         requisition.approval_role = approval_role
#         requisition.remark = remarks
#         requisition.save()

#         # Return a success response
#         return JsonResponse({'message': 'Approval status updated successfully'})

    # Redirect to the department_head view if accessed directly
    return redirect('department_head')

def workorder_list(request):
    workorders = Workorder.objects.all()
    requisition_no = request.GET.get('requisition_no')
    
   
    if requisition_no:
        workorders = Workorder.objects.filter(requisition=requisition_no)
    else:
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

def notifications(request):
    st=Issue.objects.filter(status='Initialise')
    return render(request, 'notification.html', {'st': st})

def update_issue_status(request):
     if request.method == 'POST':
        issue_no = request.POST['issue_no']
        print("Issue No:", issue_no)
        status = request.POST.get('status')
        print("Status:", status)
        status = request.POST.get('status')

        # Update the status field of the Issue object with the provided issue_no
        issue = Issue.objects.get(issue_no=issue_no)
        issue.status = status
        issue.save()

        return redirect('notifications')

    # Handle GET requests if needed



def create_store_balance(request):
    if request.method == 'POST':
        form = StoreBalanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_store_balance')
    else:
        form = StoreBalanceForm()
    return render(request, 'create_store_balance.html', {'form': form})

def create_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_purchase')
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

def requisition_list(request,username):
    requisitions = Requisition.objects.filter(user_name=username)
    return render(request, 'requisition_list.html', {'requisitions': requisitions})


def issue_list(request):
    username_filter = request.GET.get('username')
    
   
    if username_filter:
        issues = Issue.objects.filter(user_name=username_filter)
    else:
        issues = Issue.objects.filter(status="Accepted")
    issues2 = Issue.objects.filter(status="Accepted")
    
    for i in issues2:
        sb= StoreBalance.objects.filter(product_name=i.product_name)
        for j in sb:
            j.quantity=j.quantity-i.quantity
            j.save()
    return render(request, 'issue_list.html', {'issues': issues})

def store_balance_list(request):
    store_balances = StoreBalance.objects.all()
    return render(request, 'store_balance_list.html', {'store_balances': store_balances})

def purchase_list(request):
    requisition_no = request.GET.get('requisition')
    purchases = Purchase.objects.all()

    if requisition_no:
        purchases = purchases.filter(requisition=requisition_no)

    context = {
        'purchases': purchases
    }
    return render(request, 'purchase_list.html', context)

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

def product_list_list(request):
    product_lists = ProductList.objects.all()
    return render(request, 'product_list_list.html', {'product_lists': product_lists})
