"""
URL configuration for BabyFootPrintBackEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf.urls import url
from django.views import static
from django.views.generic import RedirectView

from FootPrint.views.locations_view import LocationViewSet
from BabyFootPrintBackEnd import settings
from FootPrint.views.map_setting_view import MapSettingViewSet

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('api/location/get-my-location-list/',
         LocationViewSet.as_view({'get': 'get_my_locations'})),
    path('api/location/get-my-map-settings/',
         MapSettingViewSet.as_view({'get': 'get_my_settings'})),
    path(r'', LocationViewSet.as_view({'get': 'index_page'})),
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^favicon.ico$', RedirectView.as_view(url=r'static/images/favicon.ico')),
]
    # + [re_path(ele.get('re_path'), include(ele.get('include'))) for ele in settings.PLUGINS_URL_PATTERNS]
)
