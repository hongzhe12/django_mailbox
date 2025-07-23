from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmailConfigViewSet, index, SendMailAPIView
)


router = DefaultRouter()

# 自动注册视图集路由

router.register(r'emailconfig', EmailConfigViewSet, basename='emailconfig')


urlpatterns = [
    path('', index, name='email_config'),
    path('api/', include(router.urls)),
    path('send_mail/', SendMailAPIView.as_view()),
]