from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import OCRRecord

class OCRRecordSerializer:
    class Meta:
        model = OCRRecord
        fields = ("id_num", "prefix", "firstName", "lastName", "dateOfBirth", "issueDate", "expiryDate")