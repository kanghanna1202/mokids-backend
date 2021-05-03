from django.urls import path

from movie import views

urlpatterns = [
    path('list/', views.movie_list),
    path('<int:pk>/', views.movie_detail_list),
    path('genre/', views.movie_genre_list),
    path('search/', views.SearchMovieList.as_view())
]
