from django.urls import path
from . import views, api_views

urlpatterns = [
    # Web pages
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:id>/edit/', views.post_update, name='post_update'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),

    # Auth
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # API
    path('api/posts/', api_views.post_list_create_api),
    path('api/posts/<int:id>/', api_views.post_detail_api),
    path('api/posts/<int:post_id>/comments/', api_views.comment_list_create_api),
]
