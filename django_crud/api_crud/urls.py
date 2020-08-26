from django.urls import path, include
from .views import SubjectViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subject', SubjectViewset, basename='subject')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]
