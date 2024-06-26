from django.urls import path,include
from .views import PostList, DetailPost,create_post,PostCreate,PostUpdate,PostDelete,IndexView,DetailCategory
#from django.contrib.auth.decorators import login_required
from .views import upgrade_me,subsribe_me


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
    path('registerd/', IndexView.as_view(), name='registerd'),
    path('registerd/upgrade/', upgrade_me, name ='upgrade'),
    path('category/<int:pk>/subscribe/',subsribe_me,name = 'subscribe'),
    path('category/<int:pk>/',DetailCategory.as_view(),name = 'category'),



]