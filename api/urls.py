from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import (SpectacularAPIView,SpectacularSwaggerView, SpectacularRedocView)

from apiinfo.views import User2JWTLoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('apiinfo.urls')),
    #path('token/', obtain_auth_token),
    #path('api-auth/', include('rest_framework.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema')),
    path('login/', User2JWTLoginView.as_view(), name='login'),  
]