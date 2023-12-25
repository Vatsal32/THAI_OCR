from django.urls import path, include
from .views import createOCRRecord

urlpatterns = [
    path('media/', createOCRRecord, name='Add an ID'),
]