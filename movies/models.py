from django.db import models
import datetime
from django.utils import timezone   

class Movie(models.Model):
    GENRE_CHOICES = [
        ("action", "Action"),
        ("adventure", "Adventure"),
        ("animated", "Animated"),
        ("comedy", "Comedy"),
        ("drama", "Drama"),
        ("fantasy", "Fantasy"),
        ("historical", "Historical"),
        ("romance", "Romance"),
        ("sci-fi", "Science fiction"),
        ("thriller", "Thriller"),
    ]
    STATUS_CHOICES = [
        ("coming_out", "Coming out"),
        ("finished", "Finished"),
        ("coming_soon", "Coming soon"),
    ]
    title = models.CharField(max_length=80, verbose_name="Title")
    poster = models.ImageField(verbose_name="Poster", upload_to="posters/", default="posters/default-poster.jpeg")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    rating = models.PositiveSmallIntegerField(verbose_name="Rating", default=0)
    genres = models.CharField(verbose_name="Genres", choices=GENRE_CHOICES)
    duration = models.TimeField(verbose_name="Duration")
    actors = models.CharField(verbose_name="Actors", max_length=100)
    release_date = models.DateField(verbose_name="Release date")
    status = models.CharField(verbose_name="Status", choices=STATUS_CHOICES)

    def days_left(self):
        today = timezone.now().date()
        delta = (self.release_date - today).days
        return f"{delta} days left" if delta > 0 else "Released"
    
    def __str__(self):
        return self.title