
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status
from .models import Tarea
from .serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    """
    Provee: list, create, retrieve, update (PUT/PATCH), destroy.
    Usamos ModelViewSet para cumplir todos los endpoints requeridos.
    """
    queryset = Tarea.objects.all().order_by('-created_at')
    serializer_class = TareaSerializer


# Create your views here.
