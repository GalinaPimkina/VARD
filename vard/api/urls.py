from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'access', views.AccessViewSet)
router.register(r'file', views.FileViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]