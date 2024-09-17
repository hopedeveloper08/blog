from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import LogoutView, UserListCreateView, UserRetrieveUpdateDestroyView


urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserListCreateView.as_view(), name='users'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user'),
]
