from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name="main_view"),
    path('posts/', views.post_list_view, name='post_list'),
    path('posts/<int:id>/', views.post_detail_view, name='post_detail'),
    path("posts/create/", views.post_create_view, name='post_create_view'),
]