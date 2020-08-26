from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject
from .serializers import SubjectSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, mixins, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

# Create your views here.

class SubjectViewset(viewsets.ModelViewSet):
    
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()