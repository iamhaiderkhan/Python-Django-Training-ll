from django.contrib import admin
from user_profile.models import UserProfile
from user_profile.models import SitesSettings
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(SitesSettings)
