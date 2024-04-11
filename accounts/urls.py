from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
     path('register/', views.register, name = 'register'),
     path('profile/', views.profile, name='profile'),
     path('login/', views.user_login, name='login'),
     path('logout/', views.logoutUser, name='logout'),
     path('update_plan/', views.update_plan, name='update_plan'),
     path('edit_profile/', views.edit_profile, name='edit_profile'),
     path('update_withdrawal/', views.update_withdrawal, name='update_withdrawal'),
     path('make_deposit/', views.make_deposit, name='make_deposit'),
     path('pay/', views.pay, name='pay'),
     path('bit_pay/', views.bitcoin, name='bit_pay'),
     path('eth_pay/', views.ethereum, name='eth_pay'),
     path('usdt_pay/', views.usdt, name='usdt_pay'),
     path('bank_pay/', views.bank, name='bank_pay'),

    
]