from rest_framework import viewsets

from .models import *
from .serializers import *

class MODE2LNAMEViewSet(viewsets.ModelViewSet):
    queryset = MODE2LNAME.objects.all()
    serializer_class = MODE2LNAMESerializer

class MODELNAMEViewSet(viewsets.ModelViewSet):
    queryset = MODELNAME.objects.all()
    serializer_class = MODE2LNAMESerializer