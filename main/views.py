from django.shortcuts import render, redirect
# from .forms import CreateNewPost
from .models import ArtPost
from PIL import Image


def index(response):
    return render(response, 'index.html', {})


# def create_post(response):
#   if response.method == 'POST':
#     form = CreateNewPost(response.POST, response.FILES)
#     if form.is_valid():
#       title = form.cleaned_data.get("title")
#       description = form.cleaned_data.get('description')
#       art = form.cleaned_data.get('art')
#       art_post = ArtPost.objects.create(title=title, description=description, art=art)
#       art_post.save()
#       print(response.FILES)
#       return redirect('/')
#   else:
#     form = CreateNewPost()
#   return render(response, 'create_post.html', {'form': form})


def create_post(response):
  if response.method == 'POST':
    unallowed_images = False

    art = []
    for file in response.FILES.getlist('art'):
      try:
        trial_image = Image.open(file)
        trial_image.verify()
        art.append(file)
      except Exception:
        print(file)
        unallowed_images = True
    
    if unallowed_images:
      
      title=response.POST.get('title')
      description=response.POST.get('description')
      
      return render(response, 'create_post.html', {'title': title, 'description': description})
      
    art_post = ArtPost.objects.create(
      title=response.POST.get('title'),
      description=response.POST.get('description'),
      hidden=False,
      user = response.user)

    for art in art:
      art_post.art_set.create(art=art)
    art_post.save()

    return redirect('/')
  return render(response, 'create_post.html', {'title': '', 'description': ''})

def view_post(response, id):
  post = ArtPost.objects.get(id=id)
  return render(response, 'view_post.html', {'post': post})

def view_posts(response):
  posts = ArtPost.objects.all()
  return render(response, 'view_posts.html', {'posts': posts})