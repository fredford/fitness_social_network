from ..models import Post
from ..serializers import PostSerializer

from rest_framework import viewsets, permissions



class PostViewSet(viewsets.ModelViewSet):

	permission_classes = [
		permissions.AllowAny
	]
	
	lookup_field = 'id'

	serializer_class = PostSerializer

	queryset = Post.objects.all()
