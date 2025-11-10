from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "poster", "rating", "release_date", "status")
    list_editable = ("rating", "status")
    search_fields = ("title", "release_date")
