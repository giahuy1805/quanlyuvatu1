from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import các view đăng nhập/đăng xuất của Django

urlpatterns = [
    path('', include('medical_supplies.urls')),
    path('admin/', admin.site.urls),
    path('supplies/', include('medical_supplies.urls')),  # Bao gồm URL của ứng dụng medical_supplies
    path('login/', auth_views.LoginView.as_view(template_name='medical_supplies/login.html'), name='login'),  # Đăng nhập
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Đăng xuất
]