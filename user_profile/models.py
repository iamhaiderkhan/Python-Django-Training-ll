from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    cinc_number = models.CharField(max_length=20, blank=True, verbose_name="CNIC Number")
    occupation = models.CharField(max_length=500, blank=True, verbose_name="Your Occupation")
    bio = models.TextField(max_length=500, blank=True, verbose_name="About (Bio)")
    address = models.CharField(max_length=255, blank=True, verbose_name="Permanent Address")
    contact_number = models.CharField(max_length=30, blank=True, verbose_name="Contact Number")
    city = models.CharField(max_length=30, blank=True, verbose_name="Your Location (City)")
    country = models.CharField(max_length=30, blank=True, verbose_name="Your Nationality (Country)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance, **instance.user_profile)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()