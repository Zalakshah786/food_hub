from . import views
from django.urls import path
urlpatterns = [
    path('home/', views.PostList.as_view(), name='home'),
]

#from foodhub import views as foodhub_views
#from DiscoverUs import views as DiscoverUs_views