from . import views
from django.urls import path
from .views import dashboard
from .views import Home
from .views import login_view
from .views import register_view
from .views import logout_view
from .views import post_detail
from .views import dish_detail

from .views import edit_comment
from .views import delete_comment
from foodhub import views as foodhub_views

urlpatterns = [
    path('', Home.as_view(), name='home'),   # Home page
    #path('recipes/', views.recipes, name='recipes'),  # Recipes page
    path('menu_list/', views.menu_list, name='menu_list'),  # Menu List page
    #path('chefs/', views.chefs, name='chefs'),  # Chefs page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Register page
    path('logout/', views.logout_view, name='logout'),  # Logout action
    #path('register_chef/', views.register_chef_view, name='register_chef'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),  # Post detail page
    path('dish_detail/<int:pk>/', views.dish_detail, name='dish_detail'),  # Dish detail page
    
    path('edit_comment/<int:pk>/<int:comment_id>/', views.edit_comment, name='edit_comment'),  # Edit comment page
    path('delete_comment/<int:pk>/<int:comment_id>/', views.delete_comment, name='delete_comment'),  # Delete comment action

    path('collaborate_request/', views.collaborate_request_view, name='collaborate_request'),
   
    
]


#from foodhub import views as foodhub_views
#from DiscoverUs import views as DiscoverUs_views