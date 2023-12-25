from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import OCRRecord

class OCRRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OCRRecord
        fields = ("id", "id_num", "prefix", "firstName", "lastName", "dateOfBirth", "issueDate", "expiryDate")