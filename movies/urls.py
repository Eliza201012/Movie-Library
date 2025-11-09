from django.urls import path
from .views import create_movie, movie_list, movie_detail, movie_update, movie_delete

urlpatterns = [
    path("", movie_list, name="movie_list"),
    path("create_movie/", create_movie, name="create_movie"),
    path("movie_detail/<int:id>/", movie_detail, name="movie_detail"),
    path("movie_update/<int:id>/", movie_update, name="movie_update"),
    path("movie_delete/<int:id>/", movie_delete, name="movie_delete"),
]
