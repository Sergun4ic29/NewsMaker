from django.urls import path
from .views import PostList, DetailPost,create_post,PostCreate,PostUpdate,PostDelete

urlpatterns = [
    path('', PostList.as_view(),name='post_detail'),
    path('<int:pk>',DetailPost.as_view(),name='post_detail'),
    path('nw/create/',PostCreate.as_view(),name='post_creat'),
    path('ar/create/',PostCreate.as_view(),name='post_creat'),
    #path('nw/create/',create_post,name='post_creat'),
    #path('ar/create/', create_post, name='post_creat'),
    path('ar/<int:pk>/update',PostUpdate.as_view(),name='post_update'),
    path('nw/<int:pk>/update',PostUpdate.as_view(),name='post_update'),
    path('ar/<int:pk>/delete',PostDelete.as_view(),name='post_delete'),
    path('nw/<int:pk>/delete',PostDelete.as_view(),name='post_delete'),
]