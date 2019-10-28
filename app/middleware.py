from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from user_profile.models import SitesSettings
from django.core.exceptions import ObjectDoesNotExist


class SettingsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            current_site_settings = SitesSettings.objects.get_settings_by_site(request)
            settings.EMAIL_HOST = current_site_settings.email_host
            settings.EMAIL_HOST_USER = current_site_settings.email_host_user
            settings.EMAIL_HOST_PASSWORD = current_site_settings.email_host_password
            settings.EMAIL_PORT = current_site_settings.email_port

        except ObjectDoesNotExist:
            pass
    pass


