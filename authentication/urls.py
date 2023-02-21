from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import SimpleLoginView, SimpleSignupView, SimpleLogoutView, RegisterAPIView

app_name = 'authentication'

urlpatterns = [
    path('signin/', SimpleLoginView.as_view(), name='signin'),
    path('signup/', SimpleSignupView.as_view(), name='signup'),
    path('logout/', SimpleLogoutView.as_view(), name='logout'),

    path('api/v1/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/register', RegisterAPIView.as_view(), name='register'),
]
