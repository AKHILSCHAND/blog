from django.urls import path
from . import views


urlpatterns = [
    path ('dashboard',views.dashboard, name = 'dashboard'),
# category_urls
    path ('dashboard/categories',views.categories, name = 'categories'),
    path ('dashboard/categories/add',views.add_categories, name = 'add_categories'),
    path ('dashboard/categories/edit/<int:pk>',views.edit_categories, name = 'edit_categories'),
    path ('dashboard/categories/delete/<int:pk>',views.delete_categories, name = 'delete_categories'),
# post_urls
    path ('dashboard/posts',views.posts, name = 'posts'),
    path ('dashboard/posts/add',views.add_posts, name = 'add_posts'),
    path ('dashboard/posts/edit/<int:pk>',views.edit_posts, name = 'edit_posts'),
    path ('dashboard/posts/delete/<int:pk>',views.delete_posts, name = 'delete_posts'),
  
]