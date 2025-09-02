from django.contrib import admin
from .models import Q, I, IT

# Register your models here.

class IA(admin.ModelAdmin):
    list_display = ("c", "x", "y", "h", "w")

class QA(admin.ModelAdmin):
    list_display = ("n", "rus", "eng")

class ITA(admin.ModelAdmin):
    list_display = ("q", "rus", "eng")

admin.site.register(Q, QA)
admin.site.register(I, IA)
admin.site.register(IT, ITA)