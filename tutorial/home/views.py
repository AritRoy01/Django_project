from django.shortcuts import render
from rest_framework import viewsets
from home.models import Project
from home.serializers import CompanySerializer

# Create your views here.

class CompanyViewset(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=CompanySerializer
