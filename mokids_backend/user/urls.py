from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user import views

urlpatterns = [
    path('register/', views.create_user),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
