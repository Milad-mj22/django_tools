from django.urls import path
from .views import home, profile, RegisterView,tools \
        ,my_orders,add_raw_material,post_edit_quil\
        ,create_order,add_mother_material,show_order,snapp,show_restaurant_list,\
        restaurant_food_list,add_restaurant,print_order,foodRawMaterials,addfoodrawmaterial,show_food_material

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('tools/',tools, name='tools'),
    path('tools/snapp',snapp, name='tools'),
    path('tools/foodrawmaterials',foodRawMaterials, name='foodRawMaterials'),
    path('tools/foodrawmaterials/<int:id>',show_food_material, name='foodRawMaterials'),
    path('tools/add_food_raw_material',addfoodrawmaterial, name='addfoodrawmaterial'),

    # path('tools/snapp/اصفهان/<str:res_name>',restaurant_food_list, name='tools'),

    
    path('tools/snapp/add_restaurant',add_restaurant, name='tools'),
    path('tools/snapp/<str:city>',show_restaurant_list, name='tools'),
    # path('tools/snapp/<str:city>/<str:res_name>',restaurant_food_list, name='tools'),
    path('tools/snapp/<str:city>/<str:res_name>',restaurant_food_list, name='tools'),


    path('orders/print_order/<int:id>', print_order, name='order-show'),

    
    path('profile/create_order', create_order, name='create_post'),
    path('profile/my_orders', my_orders, name='my_posts'),
    path('profile/create_material/', add_raw_material, name='add_material'),
    path('profile/create_mother_material/', add_mother_material, name='add_mother_material'),
    # path('tools/<slug:slug>/',PostDetail.as_view(), name='post_detail'),
    path('orders/edit_order/<int:id>', post_edit_quil, name='order-edit'),
    path('orders/show_order/<int:id>', show_order, name='order-show'),
    path('posts/<int:id>/', post_edit_quil, name='post-edit'),
    path('test/', create_order, name='post-create3'),




    #/////////////////////////


]
