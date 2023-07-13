from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView

from .forms import UserRegistrationForm, UserAddressForm


User = get_user_model()


class UserRegistrationView(TemplateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/user_registration.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(
                reverse_lazy('transactions:transaction_report')
            )
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        registration_form = UserRegistrationForm(self.request.POST)
        address_form = UserAddressForm(self.request.POST)

        if registration_form.is_valid() and address_form.is_valid():
            user = registration_form.save()
            address = address_form.save(commit=False)
            address.user = user
            address.save()

            login(self.request, user)
            messages.success(
                self.request,
                (
                    f'Thank You For Creating A Bank Account. '
                    f'Your Account Number is {user.account.account_no}. '
                )
            )
            return HttpResponseRedirect(
                reverse_lazy('transactions:deposit_money')
            )

        return self.render_to_response(
            self.get_context_data(
                registration_form=registration_form,
                address_form=address_form
            )
        )

    def get_context_data(self, **kwargs):
        if 'registration_form' not in kwargs:
            kwargs['registration_form'] = UserRegistrationForm()
        if 'address_form' not in kwargs:
            kwargs['address_form'] = UserAddressForm()

        return super().get_context_data(**kwargs)


class UserLoginView(LoginView):
    template_name='accounts/user_login.html'
    redirect_authenticated_user = False


class LogoutView(RedirectView):
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)




###########################

from django.shortcuts import render,HttpResponseRedirect
from . import forms
from .forms import TransactionForm
from . models import *
from decimal import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.
def send(request):
    transfer =Transfer.objects.all()
    Context ={'transfer':transfer}
    return render(request, 'accounts/send.html',Context)




def Transfermoney(request):
    if request.method == 'POST':
        form = forms.TransactionForm(request.POST)
        if form.is_valid():
            from_account_number = form.cleaned_data.get('from_account')
            to_account_number = form.cleaned_data.get('to_account')
            amount = form.cleaned_data.get('amount')

            sender = Account.objects.get(account_number=from_account_number)
            if sender.account_balance >= amount:
                # Create and save the transaction object
                trans = Transfer.objects.create(
                    owner=request.user,
                    from_account=sender,
                    to_account=to_account_number,
                    amount=amount
                )

                # Debit the sender account
                sender.account_balance -= amount
                sender.save()

                # Credit the receiver account
                receiver = Account.objects.get(account_number=to_account_number)
                receiver.account_balance += amount
                receiver.save()
                
                messages.success(request,
                 f'Successfully Transfered {"{:,.2f}".format(float(amount))}$ from your account'
        )
                return HttpResponseRedirect(reverse_lazy('send'))
    else:
        form = forms.TransactionForm()
        
    

    return render(request, "accounts/transfer.html", {'form': form})


# def send(request):
    if request.method == 'POST':
        form = forms.TransactionForm(request.POST)
        if form.is_valid():
            sender = Account.objects.get(account_number=request.POST.get('from_account'))
            if sender.account_balance > int(request.POST.get('amount')):

                # Create and save the transaction object
                trans = Transaction.objects.create(
                    owner=request.user,
                    from_account=sender,
                    to_account=request.POST.get('to_account'),
                    amount=int(request.POST.get('amount'))
                )

                # Debit the sender account
                sender.account_balance -= int(request.POST.get('amount'))
                sender.save()

                # Credit the receiver account
                receiver = Account.objects.get(account_number=request.POST.get('to_account'))
                receiver.account_balance += int(request.POST.get('amount'))
                receiver.save()

                return HttpResponseRedirect(reverse_lazy('send'))
    else:
        form = forms.TransactionForm()

    return render(request, "index.html", {'form': form})




# def send(request):

    
    if request.method == 'POST':
        form = forms.TransactionForm(request.POST)
        if form.is_valid():
            sender = Account.objects.get(account_number=request.POST.get('from_account'))
            if sender.account_balance > int(request.POST.get('amount')):

                trans =  form.save()
                trans.owner = request.user
                trans.save()

                # debit the sender account
                sender.account_balance -= int(request.POST.get('amount'))
                sender.save()

                #credit the receiver account
                receiver = Account.objects.get(account_number=request.POST.get('to_account'))
                receiver.account_balance += int(request.POST.get('amount'))
                receiver.save()

                return HttpResponseRedirect(reverse_lazy('customers:history'))
            # else:
            #     return 
    else:
        form = forms.TransactionForm()
        return render(request, "index.html", {'form': form})