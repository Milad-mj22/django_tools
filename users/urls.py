from django.urls import path
from .views import home, profile, RegisterView,tools \
        ,my_orders,add_raw_material,post_edit_quil\
        ,create_order,add_mother_material,show_order,snapp,show_restaurant_list,\
        restaurant_food_list,add_restaurant,print_order,foodRawMaterials,addfoodrawmaterial,show_food_material,night_food_order,\
        show_flow,section1_view,section2_view,section3_view,section4_view,section5_view,load_temp,CustomLogoutView,add_store,success_page,\
        show_store,submit_data,show_test,take_store,confrim_take_store,log_view_store

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
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
    path('orders/show_flow/<int:order_id>', show_flow, name='show_flow'),

    path('section1/<int:order_id>/', section1_view, name='section1_url'),
    path('section2/<int:order_id>/', section2_view, name='section2_url'),
    path('section3/<int:order_id>/', section3_view, name='section3_url'),
    path('section4/<int:order_id>/', section4_view, name='section4_url'),
    path('section5/<int:order_id>/', section5_view, name='section5_url'),


    
    path('profile/create_order', create_order, name='create_post'),
    path('profile/my_orders', my_orders, name='my_posts'),
    path('profile/create_material/', add_raw_material, name='add_material'),
    path('profile/create_mother_material/', add_mother_material, name='add_mother_material'),
    path('profile/night_order/', night_food_order, name='night_food_order'),
    # path('tools/<slug:slug>/',PostDetail.as_view(), name='post_detail'),
    path('orders/edit_order/<int:id>', post_edit_quil, name='order-edit'),
    path('orders/show_order/<int:id>', show_order, name='order-show'),
    path('posts/<int:id>/', post_edit_quil, name='post-edit'),
    path('test/', load_temp, name='post-create3'),


    path('profile/store_add/',add_store,name='add-store'),

    path('profile/store_take/',take_store,name='add-store'),
    path('profile/store_take_confirm/',confrim_take_store,name='add-store'),

    path('profile/store/',show_store,name='add-store'),
    path('profile/store_log/', log_view_store, name='logs_store'),


    path('success/', success_page, name='success_page'),  # URL for success page
    path('submit-warehouse/', show_store, name='submit-warehouse'),
    path('submit-data/', submit_data, name='submit_data'),
    path('show_test/', show_test, name='submit_data'),
    #/////////////////////////


]
