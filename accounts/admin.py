from django.contrib import admin
from accounts.models import Account,contactdetails
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class AccountInline(admin.StackedInline):
    model= Account
    can_delete= True
    verbose_name_plural = 'Accounts'


class CustomizedUserAdmin(UserAdmin):
    inlines=(AccountInline,)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
admin.site.register(Account)
admin.site.register(contactdetails)
