from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField
    director = models.ForeignKey(Director)
