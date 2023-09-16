from django.contrib import admin

from .models import Appoinment, Doctor, Patient

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appoinment)

