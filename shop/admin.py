from django.contrib import admin
from shop.models import Shoe, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3  # Number of extra inline form fields

class ShoeAdmin(admin.ModelAdmin):
    inlines = [ImageInline]  # Add inline images to Shoe admin page
    list_display = ('name', 'description', 'price')  # Define which fields to display in the list view

admin.site.register(Shoe, ShoeAdmin)
