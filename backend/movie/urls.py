from django.urls import path

from movie import views

urlpatterns = [
    path('list/', views.movie_list),
]