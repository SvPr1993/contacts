from django.contrib import admin
from .models import Shops


@admin.register(Shops)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'surname')
