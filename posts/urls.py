from django.urls import path
from . import views
from .views import post_list,post_detail,post_delete,post_create,post_update

app_name = 'posts'

urlpatterns = [
    path('' ,views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/update/', views.post_update, name='post_update'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
]
