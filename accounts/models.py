from django.db import models
from django.contrib.auth.models import User
import locale

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
TRANSACTION = (
        ('Pending', 'Pending'),
        ('Available', 'Available'),
        ('Processing', 'Processing'),
    )
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    deposit = models.FloatField(null=True, blank=True)
    interest = models.FloatField(null=True, blank=True)
    transaction = models.CharField(max_length=200, null=True, blank=True, default='Pending', choices=TRANSACTION)

    def __str__(self):
        return self.user.username

PLAN = (
        ('Rookie', 'Rookie $100 - $200'),
        ('Captain', 'Captain $210 - $500'),
        ('Veteran', 'Veteran $510 - ∞'),
    )
class Plan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=200, null=True, blank=True, choices=PLAN)

    def __str__(self):
        return self.user.username

NAME = (
        ('Bitcoin', 'Bitcoin'),
        ('Ethereum', 'Ethereum'),
        ('USDT', 'USDT'),
    )
    
class Withdrawal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_name = models.CharField(max_length=200, null=True, blank=True, choices=NAME)
    wallet_address = models.CharField(max_length=200, null=True, blank=True)

    





