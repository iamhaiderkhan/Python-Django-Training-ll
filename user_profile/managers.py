from django.db.models import Manager
from django.contrib.sites.models import Site


class UserProfileManager(Manager):

    def total_profiles(self):
        return self.count()


class SettingsManager(Manager):

    def get_settings_by_site(self, request):
        current_site = Site.objects.get_by_natural_key(request.get_host())
        return self.get(site_id=current_site.id)
