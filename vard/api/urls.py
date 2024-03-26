from django.urls import path, include
from rest_framework import routers

from . import views
from .views import ConnectAPI

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"access", views.AccessViewSet)
router.register(r"file", views.FileViewSet)
router.register(r"dashboard", views.DashboardViewSet)
router.register(r"chart", views.ChartViewSet)
router.register(r"feedback", views.FeedbackViewSet)
router.register(r"comment", views.CommentViewSet)
router.register(r"read_comment", views.ReadCommentViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/connect/", ConnectAPI.as_view())
]
