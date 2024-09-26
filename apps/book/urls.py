from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.book.views import BookAPI

router = DefaultRouter()
router.register('book', BookAPI, basename='book')

urlpatterns = [

]

urlpatterns += router.urls