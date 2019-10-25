from django.contrib import admin
from user_profile.models import UserProfile
from user_profile.models import Settings
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Settings)
