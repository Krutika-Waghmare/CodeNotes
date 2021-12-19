from django.urls import path
from . import views


urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('detail_post/<int:id>/', views.detail_post, name='detail_post'),
    path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('publish_post/<int:id>/', views.publish_post, name='publish_post'),
    path('unpublish_post/<int:id>/', views.unpublish_post, name='unpublish_post'),
    path('unpublished_posts/', views.unpublished_posts, name='unpublished_posts'),
]