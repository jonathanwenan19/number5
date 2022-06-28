from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'Products,' , views.productviewset)

urlpatterns = [
path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
path('', include(router.urls))
]