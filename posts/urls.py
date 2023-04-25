from django.urls import path
from .views import (
    post_list_view,
    post_detail_view,
    post_create_view,
    post_update_view,
    post_delete_view,
    comment_create_view,
)

app_name = 'posts'

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('<int:pk>/', post_detail_view, name='post_detail'),
    path('create/', post_create_view, name='post_create'),
    path('<int:pk>/update/', post_update_view, name='post_update'),
    path('<int:pk>/delete/', post_delete_view, name='post_delete'),
    path('<int:pk>/comment/', comment_create_view, name='comment_create'),
]
