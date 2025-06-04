
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

from hello_world.core import views as core_views

urlpatterns = [
    path("", views.contact_view, name='contact'),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    # path('contact/', contact_view, name='contact'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
