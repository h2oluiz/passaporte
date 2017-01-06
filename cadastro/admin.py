from django.contrib import admin

# Register your models here.

from .models import Atleta

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ('name',)

