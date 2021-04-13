import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related


class Post(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=2000)
	image = models.TextField(null=True, blank=True)
	published = models.DateTimeField(auto_now_add=True)
	visibility = models.CharField(max_length=50)

class Comment(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	content = models.CharField(max_length=500)
	published = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
	summary = models.CharField(max_length=100, default="Someone likes your post/comment")

class Follow(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
	follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
	friends = models.BooleanField(default=False)
	summary = models.CharField(max_length=200, default="Someone follows you")

class Inbox(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
	like = models.ForeignKey(Like, on_delete=models.CASCADE, null=True, blank=True)
	follow = models.ForeignKey(Follow, on_delete=models.CASCADE, null=True, blank=True)