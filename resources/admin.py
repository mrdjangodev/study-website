from django.contrib import admin
from .models import Resource
# Register your models here.

class ResourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'auther', 'recievers']
    
admin.site.register(Resource, ResourceAdmin)
