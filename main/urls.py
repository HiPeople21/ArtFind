from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create_post, name='create_post'),
  path('post/', views.view_posts, name='view_posts'),
  path('post/<int:id>/', views.view_post, name='view_post'),
]