from django.contrib import admin
from .models import Phone


# @admin.register(Phone)
# class PhoneAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'price', 'release_data']
admin.site.register(Phone)