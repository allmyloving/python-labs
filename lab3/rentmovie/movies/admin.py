from django.contrib import admin
from .models import Movie
from .models import Director

admin.site.register(Movie)
admin.site.register(Director)
