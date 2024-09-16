from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('api-token-auth/', obtain_auth_token, name='auth-token'),
]
