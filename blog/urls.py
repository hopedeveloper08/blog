from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user-account/', include('user_account.urls')),
    path('api/v1/blog/', include('article.urls')),
]
