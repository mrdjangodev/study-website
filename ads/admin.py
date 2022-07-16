from django.contrib import admin
from .models import Ads
# Register your models here.

class AdsAdmin(admin.ModelAdmin):
    list_display = ['id', 'auther', 'speacial_for', 'created_at']
    search_fields = ['id', 'auther', 'speacial_for']
    
admin.site.register(Ads, AdsAdmin)
