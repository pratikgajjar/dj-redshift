import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Youtube Scrapper API')

urlpatterns = [
                  url(r'^$', schema_view),
                  path('admin/', admin.site.urls),
                  # the 'api-root' from django rest-frameworks default router
                  # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
                  re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
