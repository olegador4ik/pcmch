from django.contrib import admin
from .models import Q
from .models import I

# Register your models here.

class QA(admin.ModelAdmin):
    list_display = ("q", "n")

class IA(admin.ModelAdmin):
    list_display = ("n", "c", "x", "y", "h", "w")

admin.site.register(Q, QA)
admin.site.register(I, IA)