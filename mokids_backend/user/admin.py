from django.contrib import admin

from movie.models import Movie
from user.models import User

admin.site.register(User)
admin.site.register(Movie)
