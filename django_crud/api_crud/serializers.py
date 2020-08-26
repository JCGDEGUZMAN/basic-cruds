from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        #fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']
        fields = '__all__' 