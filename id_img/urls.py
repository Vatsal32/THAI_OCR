from django.urls import path, include
from .views import (
    Id_Img_API,
)

urlpatterns = [
    path('media/', Id_Img_API.as_view()),
]