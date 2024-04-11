from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Account

@receiver(post_save, sender=User)
def create_user_accounts(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance, deposit=0.00, interest=0.00)
