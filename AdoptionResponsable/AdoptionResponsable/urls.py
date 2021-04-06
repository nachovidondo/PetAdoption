from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Index.urls')),
    path('pets/',include('Pets.urls')),
    path('login/',LoginView.as_view(template_name ="login.html"),name ="login"),
    path('logout/',LogoutView.as_view(template_name ="login.html"), name="logout"),
    path('contact/',include('Contact.urls')), 
    path('aboutus/',include('AboutUs.urls'))
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)