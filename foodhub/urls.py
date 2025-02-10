from django.urls import path, include
from . import views
from .views import (
    Home,
    dashboard,
    login_view,
    register_view,
    logout_view,
    post_detail,
    dish_detail,
    edit_comment,
    delete_comment,
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('menu_list/', views.menu_list, name='menu_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('dish_detail/<int:pk>/', views.dish_detail, name='dish_detail'),
    path('accounts/', include('allauth.urls')),
    path(
        'edit_comment/<int:pk>/<int:comment_id>/',
        views.edit_comment,
        name='edit_comment'
    ),
    path(
        'delete_comment/<int:pk>/<int:comment_id>/',
        views.delete_comment,
        name='delete_comment'
    ),
    path(
        'collaborate_request/',
        views.collaborate_request_view,
        name='collaborate_request'
    ),
]
