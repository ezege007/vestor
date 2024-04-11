from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import CreateUserForm, UserProfileForm, CustomAuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, CustomAuthenticationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import *
import locale
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Account, Plan
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import *

def register(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            # Authenticate and login the user
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('accounts:login')  # Redirect to the home page after successful registration
    else:
        user_form = CreateUserForm()
        profile_form = UserProfileForm()

    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:profile')  # Redirect to the home page after successful login
    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Account, Plan
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User

@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    try:
        user_accounts = Account.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_accounts = None

    try:
        user_plans = Plan.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_plans = None

    try:
        user_withdrawals = Withdrawal.objects.filter(user=request.user)
    except ObjectDoesNotExist:
        user_withdrawals = None

    show_message = user_accounts.deposit == 0.00 and user_plans is None

    context = {
        'user_profile': user_profile,
        'user_accounts': user_accounts,
        'user_plans': user_plans,
        'user_withdrawals': user_withdrawals,
        'show_message': show_message,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'transaction': user_accounts.transaction  # Include transaction in context
    }
    return render(request, 'accounts/profile.html', context)


def logoutUser(request):
	logout(request)
	return redirect('accounts:login')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Plan


@login_required
def update_plan(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        # Handle the case where UserProfile does not exist for the user
        return redirect('accounts:profile')  # Redirect to profile if UserProfile does not exist
    
    try:
        user_plan = Plan.objects.get(user=user)
    except Plan.DoesNotExist:
        user_plan = None
    
    if request.method == 'POST':
        form = PlanUpdateForm(request.POST, instance=user_plan)
        if form.is_valid():
            form.instance.user = user
            form.save()
            return redirect('accounts:profile')  # Redirect to profile after updating the plan
    else:
        form = PlanUpdateForm(instance=user_plan)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/update_plan.html', context)


login_required
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None
    
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user = request.user
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('accounts:profile')  # Redirect to the profile page after successful submission
    else:
        form = EditUserProfileForm(instance=user_profile)
    
    
    return render(request, 'accounts/edit_profile.html', {'form': form})


def update_withdrawal(request):
    try:
        withdrawal = Withdrawal.objects.get(user=request.user)
    except Withdrawal.DoesNotExist:
        withdrawal = None

    if request.method == 'POST':
        form = UpdateWithdrawalForm(request.POST, instance=withdrawal)
        if form.is_valid():
            withdrawal = form.save(commit=False)
            withdrawal.user = request.user
            withdrawal.save()
            return redirect('accounts:profile')  # Redirect to the profile page after successful submission
    else:
        form = UpdateWithdrawalForm(instance=withdrawal)

    return render(request, 'accounts/update_withdrawal.html', {'form': form})



def make_deposit(request):
    if request.method == 'POST':
        # Get the user's account
        account = Account.objects.get(user=request.user)

        # Get the amount to deposit from the form
        amount = float(request.POST.get('amount'))

        # Update the deposit field
        account.deposit += amount
        account.save()

        return redirect('accounts:profile')  # Redirect to a success page after deposit

    return render(request, 'accounts/make_deposit.html')

def pay(request):

    return render(request, 'accounts/pay.html')

def bitcoin(request):

    return render(request, 'accounts/bitcoin_pay.html')

def ethereum(request):

    return render(request, 'accounts/eth_pay.html')

def usdt(request):

    return render(request, 'accounts/usdt.html')

def bank(request):

    return render(request, 'accounts/bank.html')


