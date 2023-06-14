from django.urls import path
from .views import home, profile, RegisterView,tools \
    , PostList , PostDetail , toolslist , create_post\
        ,post_list_quil,post_view_quil,my_posts,post_edit_quil,test

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('tools/',tools, name='tools'),
    path('tools_new/',tools, name='tools'),
    path('profile/create_post', create_post, name='create_post'),
    path('profile/my_posts', my_posts, name='create_post'),
    path('blog/<slug:slug>/',PostDetail.as_view(), name='post_detail'),
    path('posts/<slug:slug>', post_view_quil,  name='post_view'),
    path('posts/', post_list_quil, name='post_list'),
    path('posts/edit/<int:id>/', post_edit_quil, name='post-edit'),
    path('posts/<int:id>/', post_edit_quil, name='post-edit'),
    path('test/', test, name='post-edit'),
]
