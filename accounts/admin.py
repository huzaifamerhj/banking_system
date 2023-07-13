from django.contrib import admin

from .models import BankAccountType, User, UserAddress, UserBankAccount,Transfer,Account


admin.site.register(BankAccountType)
admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(UserBankAccount)
admin.site.register(Transfer)
admin.site.register(Account)
