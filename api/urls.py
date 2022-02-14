from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('mobiles', views.MobileViewsets)
router.register('ratings', views.RatingViewsets)

urlpatterns = [
    # Viewsets for List, create, PK(retrieve, update, destroy)
    path("api/", include(router.urls)),
]