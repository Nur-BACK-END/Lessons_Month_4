from django.contrib import admin
from django.urls import path
from posts.views import main_view, list_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = (
    [
    path('admin/', admin.site.urls),
    path('' , main_view),
    path('posts/', list_view),
    ]
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
