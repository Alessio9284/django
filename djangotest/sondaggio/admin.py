from django.contrib import admin

# Register your models here.
from .models import Domanda,Scelta

admin.site.register(Domanda)
admin.site.register(Scelta)