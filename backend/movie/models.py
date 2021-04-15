from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=50)
    grade = models.CharField(max_length=8)
