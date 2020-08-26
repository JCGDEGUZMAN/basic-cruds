from django.urls import path, include
from .views import genericAPIView

urlpatterns = [
    path('subject/', genericAPIView.as_view()),
    path('subject/<int:id>', genericAPIView.as_view()),
]
