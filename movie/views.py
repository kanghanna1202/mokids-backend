import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from movie.models import Movie
from movie.serializers import MovieSerializer, MovieDetailSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    movie = Movie.objects.order_by('?')[:5]
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail_list(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {"request": request}
    serializer = MovieDetailSerializer(movie, context=context)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def watched(request, pk):
    instance = get_object_or_404(Movie, pk=pk)
    user = request.user

    if instance.watched_user.filter(id=user.id).exists():
        instance.watched_user.remove(user)
        message = 'false'
    else:
        instance.watched_user.add(user)
        message = 'true'

    context = {'watched': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_genre_list(request, genre):
    try:
        movie = Movie.objects.filter(genre__icontains=genre)
    except Movie.DoesNotExist:
        return Response({'error': {
            'code': 404,
            'message': 'Movie not found'
        }}, status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class SearchMovieList(generics.ListCreateAPIView):
    search_fields = ['title', 'keyword']
    filter_backends = (filters.SearchFilter, )
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
