from django.contrib import admin
from multapp.models.municipality import Municipality
from multapp.models.infraction import Infraction


admin.site.register(Municipality)
admin.site.register(Infraction)