from __future__ import absolute_import

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView

from pykeg.web.account import urls as account_urls
from pykeg.web.api import urls as api_urls
from pykeg.web.kbregistration import urls as kbregistration_urls
from pykeg.web.kegadmin import urls as kegadmin_urls
from pykeg.web.kegweb import urls as kegweb_urls
from pykeg.web.setup_wizard import urls as setup_wizard_urls

urlpatterns = [
    re_path(r"^api/(?:v1/)?", include(api_urls)),
    path("account/", include(account_urls)),
    path("accounts/", include(kbregistration_urls)),
    path("kegadmin/", include(kegadmin_urls)),
    # Shortcuts
    url(r"^link/?$", RedirectView.as_view(pattern_name="kegadmin-link-device")),
]

if "pykeg.web.setup_wizard" in settings.INSTALLED_APPS:
    urlpatterns += [
        path("setup/", include(setup_wizard_urls)),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.PRODUCTION:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
if settings.KEGBOT_ENABLE_ADMIN:
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]

# main kegweb urls
urlpatterns += [
    path("", include(kegweb_urls)),
]
