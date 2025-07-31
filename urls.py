from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SendMailAPIView, EmailConfigViewSet
)

router = DefaultRouter()

# 自动注册视图集路由

router.register(r'emailconfig', EmailConfigViewSet, basename='emailconfig')

urlpatterns = [
    path('send_mail/', SendMailAPIView.as_view()),
    path('', include(router.urls)),
]
