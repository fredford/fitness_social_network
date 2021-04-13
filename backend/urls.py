from rest_framework import routers, urlpatterns
from django.urls import path

from .apis import *

router = routers.DefaultRouter()
router.register('api/posts', PostViewSet, 'posts')

urlpatterns = router.urls


#urlpatterns = [
#	path('api', PostViewSet.as_view(), name='post_view')
#]