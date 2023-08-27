from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PasswordViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('passwords', PasswordViewSet, basename='passwords')

urlpatterns = [
    path('api/', include(router.urls)),
] + static('static', document_root='static')
