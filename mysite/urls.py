from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from register import views as v

urlpatterns = [
  path('admin/', admin.site.urls),
  path('register/', v.register, name='register'),
  path('', include('main.urls')),
  path('', include('django.contrib.auth.urls')), 
  path('accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
