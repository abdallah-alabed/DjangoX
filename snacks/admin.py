from django.contrib import admin
from .models import Snack

@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    search_field=['name']
    list_display=['name','description','purchaser']
    