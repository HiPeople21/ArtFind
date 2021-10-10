from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.

def accounts_view(response):
  User = get_user_model()
  users = User.objects.all()
  return render(response, 'accounts_view.html', {'users': users})

def profile_view(response):
  user = response.user
  return render(response, 'profile_view.html', {'user': user})
  