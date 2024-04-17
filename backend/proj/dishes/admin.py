from django.contrib import admin
from . import models


class DishAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'ingredients', 'recipe', 'cooktime', 'images']
    list_editable = ['name', 'ingredients', 'recipe', 'cooktime', 'images']

admin.site.register(models.Dishes, DishAdmin)
