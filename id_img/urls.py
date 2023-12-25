from django.urls import path, include
from .views import createOCRRecord, getOCRRecord, updateOCRRecord, deleteOCRRecord

urlpatterns = [
    path('media/', createOCRRecord, name='add-items'),
    path('records/', getOCRRecord, name='view_items'),
    path('update/<int:pk>/', updateOCRRecord, name='update-items'),
    path('delete/<int:pk>/', deleteOCRRecord, name='delete-items'),
]