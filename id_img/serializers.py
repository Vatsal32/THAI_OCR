from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import MyModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MyModelSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = MyModel
        fields = ['id', 'creator', 'creator_id', 'title', 'description', 'image_url']
