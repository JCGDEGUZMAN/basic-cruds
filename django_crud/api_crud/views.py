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
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# Create your views here.

class SubjectViewset(viewsets.ViewSet):
    
    def list(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
         queryset = Subject.objects.all()
         subject = get_object_or_404(queryset, pk=pk)
         serializer = SubjectSerializer(subject)
         return Response(serializer.data)
    
    def update(self, request, pk=None):
        subject = Subject.objects.get(pk=pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
            subject = Subject.objects.get(pk=pk)
            subject.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)