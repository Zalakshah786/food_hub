from . import views
from django.urls import path
from .views import dashboard
from .views import Home
urlpatterns = [
    path('', Home.as_view(), name='home'),   # Home page
    #path('recipes/', views.recipes, name='recipes'),  # Recipes page
    #path('menu_list/', views.menu_list, name='menu_list'),  # Menu List page
    #path('chefs/', views.chefs, name='chefs'),  # Chefs page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Register page
    path('logout/', views.logout_view, name='logout'),  # Logout action
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),  # Post detail page
]


#from foodhub import views as foodhub_views
#from DiscoverUs import views as DiscoverUs_views