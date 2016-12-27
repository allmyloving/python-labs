from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Movie


def index(request):
    latest_movies = Movie.objects.order_by('name')
    context = {
        'sorted_movie_list': latest_movies
    }
    return render(request, 'movies/index.html', context)


def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "movies/details.html", {'movie': movie})
