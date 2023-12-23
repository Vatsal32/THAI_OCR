from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class MyModel(models.Model):
    # creator = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="listings")
    # title = models.CharField(
    #     max_length=80, blank=False, null=False)
    # description = models.TextField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # creation_date = models.DateTimeField(auto_now_add=True)