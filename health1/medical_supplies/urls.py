from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'), 
    path('index', views.index, name='index'), 
    path('register/', views.register, name='register'), 
    path('danh-sach-thuoc/', views.danh_sach_thuoc, name='danh_sach_thuoc'),
    path('sua-thuoc/<int:thuoc_id>/', views.sua_thuoc, name='sua_thuoc'),
    path('xoa-thuoc/<int:thuoc_id>/', views.xoa_thuoc, name='xoa_thuoc'),
    path('them-thuoc/', views.them_thuoc, name='them_thuoc'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('tao-don-thuoc/', views.tao_don_thuoc, name='tao_don_thuoc'),
    path('danh-sach-don-thuoc/', views.danh_sach_don_thuoc, name='danh_sach_don_thuoc'),
]
