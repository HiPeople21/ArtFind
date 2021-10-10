from django.urls import path
from . import views

urlpatterns = [
  path('', views.accounts_view, name='accounts_view'),
  path('profile/', views.profile_view, name='profile_view'),
]