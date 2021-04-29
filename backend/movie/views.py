from rest_framework import status, generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from movie.models import Movie
from movie.serializers import MovieSerializer, MovieDetailSerializer


# 1. 메인 페이지에서 랜덤으로 영화 추천 받는 것. 영화 10개 랜덤으로 리턴 필요.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    movie = Movie.objects.order_by('?')[:10]
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 2. 상세정보 보내기. pk로 영화 상세 정보 요청 가능. 모든 정보 리턴하기 + 내가 봤는지 boolean으로 표시.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail_list(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': {
            'code': 404,
            'message': 'Movie not found'
        }}, status=status.HTTP_404_NOT_FOUND)

    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 3. 장르별로 영화 보여주기
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_genre_list(request, genre):
    try:
        movie = Movie.objects.filter(genre=genre)
    except Movie.DoesNotExist:
        return Response({'error': {
            'code': 404,
            'message': 'Movie not found'
        }}, status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 3. 영화명, 키워로 검색하기.
class SearchMovieList(generics.ListCreateAPIView):
    search_fields = ['title', 'keyword']
    filter_backends = (filters.SearchFilter, )
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
