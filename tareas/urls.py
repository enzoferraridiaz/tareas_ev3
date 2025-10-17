from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tareas.views import TareaViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
