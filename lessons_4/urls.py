from django.contrib import admin
from django.urls import path
from posts.views import main_view, list_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , main_view),
    path('posts/', list_view),
]