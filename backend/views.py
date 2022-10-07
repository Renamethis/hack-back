
from .serializers import TempSerializer
from .models import Temp
from rest_framework import viewsets

class TempViewset(viewsets.ModelViewSet):
    queryset = Temp.objects.all()
    serializer_class = TempSerializer
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']