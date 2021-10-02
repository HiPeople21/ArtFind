from django.shortcuts import render, redirect
from .forms import CreateNewPost
from .models import ArtPost

def index(response):
  return render(response, 'index.html', {})

def create_post(response):
  if response.method == 'POST':
    form = CreateNewPost(response.POST, response.FILES)
    if form.is_valid():
      title = form.cleaned_data.get("title")
      description = form.cleaned_data.get('description')
      art = form.cleaned_data.get('art')
      art_post = ArtPost.objects.create(title=title, description=description, art=art)
      art_post.save()
      print(art_post)
      return redirect('/')
  else:
    form = CreateNewPost()
  return render(response, 'create_post.html', {'form': form})