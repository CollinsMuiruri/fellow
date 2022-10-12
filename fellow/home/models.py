from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        BUYER = "BUYER", "Buyer"
        SELLER = "SELLER", "Seller"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

# Buyer Models
class BuyerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.BUYER)


class Buyer(User):

    base_role = User.Role.BUYER
    buyer = BuyerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for buyers mate!"

class BuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    buyer_nick_name = models.CharField(max_length = 50, null=True, blank=True)

@receiver(post_save, sender = Buyer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'BUYER':
        BuyerProfile.objects.create(user=instance)


# Seller models
class SellerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SELLER)


class Seller(User):

    base_role = User.Role.SELLER
    seller = SellerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for sellers mate!"

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    seller_nick_name = models.CharField(max_length = 50, null=True, blank=True)

@receiver(post_save, sender = Seller)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'SELLER':
        SellerProfile.objects.create(user=instance)

class Job(models.Model):
    name = models.CharField(max_length = 50, null=False)
    job_buyer = models.ManyToManyField(BuyerProfile, blank=True)
    job_seller = models.ManyToManyField(SellerProfile, blank=True)

    def __string__(self):
        return self.name