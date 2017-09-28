from django.contrib.auth import admin as authadmin
from django.contrib import admin
from .models import CustomUser


class UserAdmin(authadmin.UserAdmin):

    list_display = ('id', 'username', 'role')
    list_filter = ()
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('username', 'password', 'name', 'surname', 'role')}),
    )

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
