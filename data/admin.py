from django.contrib import admin
from .models import HexData

class DataAdmin(admin.ModelAdmin):
    list_display = ('id','hex_data')

# Register your models here.
admin.site.register(HexData, DataAdmin)