from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from smtplib import SMTPException
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.validators import RegexValidator
import logging
# Create your models here.

# Import managers
from .managers import UserProfileManager, SettingsManager


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

    objects = UserProfileManager()


@receiver(post_save, sender=User)
def send_email_to_new_user(sender, instance, created, **kwargs):
    if created:
        try:
            send_mail(
                'New Account',
                'Welcome to Python training Application.',
                settings.EMAIL_HOST_USER,
                [instance.email],
                fail_silently=False
            )
        except SMTPException:
            pass
        logging.info(settings.EMAIL_HOST_USER)
        logging.info("Email Successfully Sent to:", instance.email)


class SitesSettings(models.Model):
    email_host = models.CharField(max_length=255, default='')
    email_host_user = models.CharField(max_length=255)
    email_host_password = models.CharField(max_length=500)
    email_port = models.CharField(max_length=3, validators=[RegexValidator(
        regex=r'[0-9]{3}',
        message="Email post is not valid. Email post format should be 000 in digits."
    )])
    site = models.OneToOneField(Site, related_name='settings', on_delete=models.CASCADE)

    objects = SettingsManager()

    def __str__(self):
        return self.site.name



