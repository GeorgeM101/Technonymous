from django.urls import path
from .views import post_list,post_detail,post_delete,post_create,post_update

app_name = 'posts'

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('create/', post_create, name='post_create'),
    path('<int:pk>/update/', post_update, name='post_update'),
    path('<int:pk>/delete/', post_delete, name='post_delete'),
]
