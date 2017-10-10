from django.contrib import admin
from .models import HexData, VariableConfig, DataModelConfig

class DataAdmin(admin.ModelAdmin):
    list_display = ('id','hex_data')

class VariableConfigAdmin(admin.ModelAdmin):
    list_display = [f.name for f in VariableConfig._meta.fields]

# Register your models here.
admin.site.register(HexData, DataAdmin)
admin.site.register(VariableConfig, VariableConfigAdmin)
admin.site.register(DataModelConfig)