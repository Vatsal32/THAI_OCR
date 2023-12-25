from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class MyModel(models.Model):
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

class OCRRecord(models.Model):
    id = models.AutoField(primary_key=True)
    id_num = models.CharField(max_length=13)
    prefix = models.CharField(max_length=256)
    firstName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    dateOfBirth = models.CharField(max_length=256)
    issueDate = models.CharField(max_length=256)
    expiryDate = models.CharField(max_length=256)
