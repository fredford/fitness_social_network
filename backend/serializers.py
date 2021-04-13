
from backend.models import Comment, Follow, Inbox, Like, Post

from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username')

class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = '__all__'
