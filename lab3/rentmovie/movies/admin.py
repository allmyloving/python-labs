from django.contrib import admin
from .models import Movie
from .models import Director


class MovieAdmin(admin.ModelAdmin):
    fields = ['name', 'year', 'director']
    list_display = ('name', 'year', 'get_director_name')
    list_filter = ['director__name']
    search_fields = ['name']

    def get_director_name(self, movie):
        return movie.director.name


class DirectorAdmin(admin.ModelAdmin):
    fields = ['name', 'movies']
    list_display = ['name', 'get_movies']
    search_fields = ['name']

    def get_movies(self, director):
        return list(map(lambda movie: movie.name, Movie.objects.filter(director=director)))


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
