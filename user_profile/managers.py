from django.db.models import Manager
from django.contrib.sites.models import Site


class UserProfileManager(Manager):

    def total_profiles(self):
        return self.count()


class SettingsManager(Manager):

    def  get_site_id(self, site_domain):
        current_domain = Site.objects.get_by_natural_key(site_domain)
        return current_domain.id

    def get_current_settings(self, current_site_id):
        return self.get(site_id=current_site_id)



