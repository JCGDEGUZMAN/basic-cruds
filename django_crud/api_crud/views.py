from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject
from .serializers import SubjectSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class SubjectListAPIView(APIView):
    
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class SubjectDetailAPIView(APIView):
        
    def get_subject(self, id):
        try:
            return Subject.objects.get(id=id)
        except Subject.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        subject = self.get_subject(id)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, id):
        subject = self.get_subject(id)
        serializer = SubjectSerializer(subject,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        subject = self.get_subject(id)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)