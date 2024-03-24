from django.urls import path
from .views import PostList, DetailPost

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>',DetailPost.as_view(),name='post'),
]