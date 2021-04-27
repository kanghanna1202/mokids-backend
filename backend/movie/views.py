# 1. 메인 페이지에서 랜덤으로 영화 추천 받는 것. 영화 10개 랜덤으로 리턴 필요.
# 2. 상세정보 보내기. movieCd로 영화 상세 정보 요청 가능. 모든 정보 리턴하기 + 내가 봤는지 boolean으로 표시
# 3. 장르별로 검색하기. 장르 보내면 그거 맞는거 보내기
from rest_framework.views import APIView


class MovieView(APIView):
    pass
