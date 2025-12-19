from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Blog app URLs (this includes register, login, logout)
    path('', include('blog.urls')),

    # Django built-in auth (password reset/change etc.)
    path('accounts/', include('django.contrib.auth.urls')),
]
