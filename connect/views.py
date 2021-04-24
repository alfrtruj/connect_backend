from django.shortcuts import render
from .models import File
from .serializers import FileSerializer
from rest_framework import viewsets

# Create your views here.

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

