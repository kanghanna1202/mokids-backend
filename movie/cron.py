from urllib.parse import urlencode, quote_plus, unquote

import bs4
import requests

from mokids_backend import my_settings
from movie.models import Movie


def movie_list():
    service_key = my_settings.MOVIE_SERVICE_KEY

    url = 'http://open.kmrb.or.kr/openapi-data/service/MvResultService/mvResult'

    query_params = '?' + urlencode({quote_plus('ServiceKey'): service_key,
                                   quote_plus('pageNo'): '1', quote_plus('numOfRows'): '20'})

    get_data = requests.get(url + unquote(query_params))
    soup = bs4.BeautifulSoup(get_data.content, 'html.parser')

    data = soup.find_all('item')

    for item in data:
        title = item.find('usetitle')
        grade = item.find('gradename')
        director = item.find('direname')
        prod_name = item.find('prodcname')
        if grade.get_text() == '전체관람가':
            movie_detail(title.get_text(), director.get_text(), prod_name.get_text())


def movie_detail(title, director, prod_name):
    service_key = my_settings.DETAIL_SERVICE_KEY

    url = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2'

    query_params = '&' + urlencode({quote_plus('listCount'): 1,
                                    quote_plus('title'): title,
                                    quote_plus('director'): director,
                                    quote_plus('company'): prod_name,
                                    quote_plus('detail'): 'N',
                                    quote_plus('ServiceKey'): service_key})

    get_data = requests.get(url + unquote(query_params)).json()

    data = get_data['Data'][0]['Result']

    for i in data:
        movie = Movie.objects.create(
            title=title,
            genre=i['genre'],
            runtime=i['runtime'],
            plot=i['plots']['plot'][0]['plotText'],
            keywords=i['keywords'],
            posterUrl=i['posters']
        )
