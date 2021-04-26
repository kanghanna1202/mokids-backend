from django.conf import settings
from django.db import models


class Movie(models.Model):
    movieCd = models.IntegerField(primary_key=True)
    movieNm = models.CharField(max_length=20)
    genreNm = models.CharField(max_length=10)
    watchGradeNm = models.CharField(max_length=10)

    watched_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='watched_user',
        through='WatchedUser',
    )


class WatchedUser(models.Model):
    shop_post = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

