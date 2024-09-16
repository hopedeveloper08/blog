from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterView, LogoutView, ProfilesView, ProfileView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('api-token-auth/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfilesView.as_view(), name='profiles'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
