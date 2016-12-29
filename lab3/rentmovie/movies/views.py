from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Movie
from .models import Director


def index(request):
    latest_movies = Movie.objects.order_by('name')
    context = {
        'sorted_movie_list': latest_movies
    }
    return render(request, 'movies/index.html', context)


def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    director_list = Director.objects.all()
    return render(request, "movies/details.html", {'movie': movie, 'director_list': director_list})


def update(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    year = request.POST['year']
    director_id = request.POST.get('director', '')
    if request.POST['name']:
        movie.name = request.POST['name']
    if year and is_number(year):
        movie.year = year
    if director_id and director_exists(director_id):
        movie.director_id = director_id
    movie.save()
    return details(request, movie_id)


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def director_exists(director_id):
    try:
        Director.objects.get(pk=director_id)
        return True
    except Director.DoesNotExist:
        return False
