from django.urls import path

from authentication.views import SimpleLoginView, SimpleSignupView, SimpleLogoutView

app_name = 'authentication'

urlpatterns = [
    path('signin/', SimpleLoginView.as_view(), name='signin'),
    path('signup/', SimpleSignupView.as_view(), name='signup'),
    path('logout/', SimpleLogoutView.as_view(), name='logout'),
]
