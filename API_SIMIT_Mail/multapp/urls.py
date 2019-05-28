from django.urls import path
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from .views import notification

schema_view = get_swagger_view(title='MAIL API')


urlpatterns = [
    path('front/betsy/irish/embargo/admin/', admin.site.urls),

    # Swagger API
    path(
        'api/',
        schema_view,
        name='api'
    ),
    # notification
    path(
        'notification/',
        notification.NotificationServicesRest.as_view(),
        name=notification.NotificationServicesRest.name
    ),
]
