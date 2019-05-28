from django.urls import path
from django.contrib import admin
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view

from multapp.views import municipality
from multapp.views import infraction
from multapp.views import notification

schema_view = get_swagger_view(title='SIMIT WEB API')


urlpatterns = [
    path('front/betsy/irish/embargo/admin/', admin.site.urls),

    # Swagger API
    path(
        'api/',
        schema_view,
        name='api'
    ),
    # municipality
    path(
        'municipality/',
        municipality.MunicipalityList.as_view(),
        name=municipality.MunicipalityList.name
    ),
    re_path(
        '^municipality/(?P<pk>[0-9]+)/$',
        municipality.MunicipalityDetail.as_view(),
        name=municipality.MunicipalityDetail.name
    ),
    # infraction
    path(
        'infraction/',
        infraction.InfractionList.as_view(),
        name=infraction.InfractionList.name
    ),
    re_path(
        '^infraction/(?P<pk>[0-9]+)/$',
        infraction.InfractionDetail.as_view(),
        name=infraction.InfractionDetail.name
    ),
    # notification
    path(
        'notification/',
        notification.NotificationServicesRest.as_view(),
        name=notification.NotificationServicesRest.name
    ),
]
