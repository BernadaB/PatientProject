from django.contrib import admin

from .models import Record, Patient

admin.site.register(Patient)
admin.site.register(Record)
