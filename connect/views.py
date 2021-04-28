from django.shortcuts import render
from .models import File
from .serializers import FileSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.order_by('-id') # descending order by id
    serializer_class = FileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['filename', 'aippackage', 'date']

