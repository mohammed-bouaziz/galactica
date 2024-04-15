from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RouteViewset

router = DefaultRouter()

router.register(r'all_routes_crud', RouteViewset, basename="crud")


urlpatterns = [
    path('', include(router.urls))
]
