import json
import urllib

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend import my_settings


@permission_classes([AllowAny])
@api_view(['GET'])
def movie_list(request):

    service_key = my_settings.SERVICE_KEY

    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"\
          + "?key=" + service_key

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        dict = json.loads(response_body.decode('utf-8'))
        return Response(dict['movieListResult']['movieList'], status=status.HTTP_200_OK)
    else:
        return Response(rescode, status=status.HTTP_400_BAD_REQUEST)
