from django.contrib import admin
from login.models import FormData

class LoginAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'address')

admin.site.register(FormData, LoginAdmin)