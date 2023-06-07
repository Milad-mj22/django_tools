from django.urls import path
from .views import home, profile, RegisterView,tools , PostList , PostDetail , toolslist

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('tools/',tools, name='tools'),
    path('blog/', PostList.as_view(), name='blog'),
    path('<slug:slug>/',PostDetail.as_view(), name='post_detail'),
]
