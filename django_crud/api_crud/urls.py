from django.urls import path, include
from .views import SubjectListAPIView, SubjectDetailAPIView

urlpatterns = [
    path('subject/', SubjectListAPIView.as_view()),
    path('subject/<int:id>', SubjectDetailAPIView.as_view()),
]
