from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LibraryUserViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', LibraryUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
