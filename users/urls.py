from django.urls import path
from .views import home, profile, RegisterView,tools , PostList , PostDetail , toolslist , create_post,post_list_quil,post_view_quil

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('tools/',tools, name='tools'),
    path('tools_new/',tools, name='tools'),
    path('blog/', PostList.as_view(), name='blog'),
    path('form_view/', create_post, name='form_view'),
    path('blog/<slug:slug>/',PostDetail.as_view(), name='post_detail'),
    path('posts2/', post_list_quil, name='post_list'),
    path('posts2/<int:post_id>', post_view_quil,  name='post_view'),
]
