from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Blog app URLs
    path('', include('blog.urls')),  # योले blog/urls.py भित्रको सबै URL handle गर्छ

    # Authentication URLs (Django built-in)
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password change/reset

    # Custom registration view
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),       # optional, अगर default login override गर्नु छ भने
    path('logout/', views.logout_view, name='logout'),    # optional
]
