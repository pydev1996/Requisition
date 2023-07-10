from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm
from .models import Approval,Requisition,Report,Workorder,Issue,ProductList,Purchase,StoreBalance,DepartmentList

class CustomUserAdmin(UserAdmin):
    #change_form_template = 'admin/auth/user/change_form.html'
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('username', 'email', 'user_type')
    def get_plain_text_password(self, obj):
        return obj.plain_text_password

    get_plain_text_password.short_description = 'Plain Text Password'
    get_plain_text_password.admin_order_field = 'plain_text_password'

    list_display = UserAdmin.list_display + ('get_plain_text_password',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'user_type','photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'user_type'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ProductList)
admin.site.register(DepartmentList)
#admin.site.register(StoreBalance)
# admin.site.register(Approval)
#admin.site.register(Requisition)
# admin.site.register(Report)
# admin.site.register(Workorder)
#admin.site.register(Issue)
# admin.site.register(Purchase)
