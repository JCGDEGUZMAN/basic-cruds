from django.urls import path, include
from .views import subject_list, subject_detail

urlpatterns = [
    path('subject/', subject_list),
    path('subject/<int:pk>', subject_detail),
]
