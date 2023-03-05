
from django.urls import path
from posts.api.views import posts_api, post_api
from posts.api.drf_views import posts_resource, post_resource
urlpatterns=[
    # path('', posts_api, name='api.posts' ),
    # path('<int:id>', post_api, name='api.post' )
    path('', posts_resource, name='api.posts'),
    path('<int:id>', post_resource, name='api.post')
]