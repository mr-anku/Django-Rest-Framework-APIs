
from rest_framework import serializers

from demoapp.models import Post, User

"""Model Serializers"""
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','description','user']

class UserSerializer(serializers.ModelSerializer):
    post = PostSerializer(many = True, read_only= True)
    class Meta:
        model = User
        fields = ["id","name","city","post"]



