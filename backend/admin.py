from .models import Post

from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin



# Register your models here.
class PostAdmin(ModelAdmin):
	list_display=('id', 'get_user', 'get_user_id', 'title')

	def get_user(self, post):
		return post.user.username

	def get_user_id(self, post):
		return post.user.id

	get_user.short_description = 'User'
	get_user_id.short_description = 'UserID'


admin.site.register(Post, PostAdmin)