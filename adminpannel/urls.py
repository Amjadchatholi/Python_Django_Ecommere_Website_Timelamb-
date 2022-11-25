from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_login, name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('admin_home/',views.admin_home, name='adminhome'),
    path('admin_user/',views.admin_user_manage, name='admin_user'),
    path('block_user/<int:pk>',views.block_user, name='block_user'),
    path('unblock_user/<int:pk>',views.unblock_user, name='unblock_user'),

    path('admin_UserProfile', views.admin_UserProfile, name='admin_UserProfile'),
    

    path('view_product/',views.view_product, name='view_product'),
    path('edit_product/<str:slug>',views.edit_product, name='edit_product'),
    path('add_product/',views.addproduct, name='add_product'),

    path('pending_product_manage/<int:id>', views.admin_vendor_addproduct_accept, name='pending_product_manage'),

    path('view_vendor_pending_product/',views.view_vendor_pending_product,name='view_vendor_pending_product'),

    path('view_unlisted_product_admin/',views.view_unlisted_product_admin, name='view_unlisted_product_admin'),
    path('unlist_product_manage_admin/<int:id>',views.unlist_product_manage_admin, name='unlist_product_manage_admin'),

    
    path('add_category/', views.add_category, name='add_category'),
    
    path('view_category/', views.view_category, name='view_category'),


    

    path('product_order/', views.product_order, name = 'product_order_admin'),
    path('accepted_order/', views.accepted_order, name = 'accepted_order_admin'),
    path('cancel_order/', views.canceld_product_order, name = 'canceld_order_admin'),
    path('soldproduct_list/', views.soldproduct_list, name = 'soldproduct_list_admin'),

    path('order_confirm/<int:id>', views.order_confirm, name ='order_confirm_admin'),
    path('order_completed/<int:id>', views.order_completed, name ='order_completed_admin'),
]
