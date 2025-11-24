from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('appusers.urls'), name = 'appusers_urls'), # estamos linkando o arquivo url do projeto a url principal.
    # URLs do allauth (ex: /accounts/google/login/)
    path("accounts/", include("allauth.urls")),
    
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)