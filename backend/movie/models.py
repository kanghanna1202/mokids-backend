from django.conf import settings
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=20, unique=True)
    genre = models.CharField(max_length=10)
    runtime = models.CharField(max_length=10)
    plot = models.TextField()
    keywords = models.CharField(max_length=50)
    posterUrl = models.ImageField(blank=False, null=False)

    watched_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='watched_user',
        through='WatchedUser',
    )


class WatchedUser(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
