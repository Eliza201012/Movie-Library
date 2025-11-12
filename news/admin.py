from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "photo", "created_at", "updated_at")
    search_fields = ("title", "created_at")