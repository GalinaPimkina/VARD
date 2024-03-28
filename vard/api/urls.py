from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"access", views.AccessViewSet)
router.register(r"files", views.FileViewSet)
router.register(r"dashboard", views.DashboardViewSet)
router.register(r"chart", views.ChartViewSet)
router.register(r"feedback", views.FeedbackViewSet)
router.register(r"comment", views.CommentViewSet)
router.register(r"read_comment", views.ReadCommentViewSet)
router.register(r"add_connect", views.ConnectViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/connect/", views.ConnectAPI.as_view()),
    # path("api/files/", views.FileAPI.as_view())
]
