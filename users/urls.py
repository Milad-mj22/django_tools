from django.urls import path
from .views import home, profile, RegisterView,tools \
        ,post_list_quil,post_view_quil,my_posts,post_edit_quil\
        ,full_create_post_tiny,projects_list,project_view

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('tools/',tools, name='tools'),
    path('profile/create_post', full_create_post_tiny, name='create_post'),
    path('profile/my_posts', my_posts, name='my_posts'),
    # path('tools/<slug:slug>/',PostDetail.as_view(), name='post_detail'),
    path('posts/<slug:slug>', post_view_quil,  name='post_view'),
    path('posts/', post_list_quil, name='post_list'),
    path('posts/edit/<int:id>/', post_edit_quil, name='post-edit'),
    path('posts/<int:id>/', post_edit_quil, name='post-edit'),
    path('test/', full_create_post_tiny, name='post-create3'),
    path('phone_book/', tools, name='post-create3'),
    path('projects/', projects_list, name='post-create3'),
    path('projects/<int:id>/', project_view, name='project_view'),
    # path('test/', create_post_test, name='post-edit'),
]
