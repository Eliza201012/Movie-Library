from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Movie
from .forms import MovieForm

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin, login_url="accounts:login")
def create_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:movie_list")
    else:
        form = MovieForm()
    return render(request, "movies/movie_form_admin.html", {"form" : form})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movies/movies_list.html", {"movies" : movies})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, "movies/movie_detail.html", {"movie" : movie})

@user_passes_test(is_admin, login_url="accounts:login")
def movie_update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movies:movie_list")
    else:
        form = MovieForm(instance=Movie)
    return render(request, "movies/movie_form_admin.html", {"form" : form})

@user_passes_test(is_admin, login_url="accounts:login")
def movie_delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        movie.delete()
        return redirect("movies:movie_list")
    return render(request, "movies/movie_confirm_delete.html", {"movie" : movie})