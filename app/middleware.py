from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from user_profile.models import Settings
from django.core.exceptions import ObjectDoesNotExist


class SettingsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            print(request.get_host())
            current_site_domain_id = Settings.objects.get_site_id(request.get_host())
            try:
                current_site_settings = Settings.objects.get_current_settings(current_site_domain_id)
                settings.EMAIL_HOST = current_site_settings.email_host
                settings.EMAIL_HOST_USER = current_site_settings.email_host_user
                settings.EMAIL_HOST_PASSWORD = current_site_settings.email_host_password
                settings.EMAIL_PORT = current_site_settings.email_port
            except ObjectDoesNotExist:
                pass
        except ObjectDoesNotExist:
            pass
    pass


