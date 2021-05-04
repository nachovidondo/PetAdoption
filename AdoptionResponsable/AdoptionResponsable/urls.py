from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Index.urls')),
    path('pets/',include('Pets.urls')),
    path('contact/',include('Contact.urls')), 
    path('aboutus/',include('AboutUs.urls')),
    path('administration/',include('Administration.urls')),
    path('profile/', include('Profile.urls')),
    path('posts/',include('Post.urls'))
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)