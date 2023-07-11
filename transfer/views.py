from django.shortcuts import render

from accounts.models import UserBankAccount


# Create your views here.

def transfer(request):
    
    userbankaccount = UserBankAccount.objects.all()
    context ={'userbankaccount': userbankaccount}
    
    return render(request, 'transfer/transfer.html',context)

def maketransfer(request):
    
    
    
    
    return render(request, 'transfer/maketransfer.html')
