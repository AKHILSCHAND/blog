from django.urls import path
from . import views


urlpatterns = [
    path ('dashboard',views.dashboard, name = 'dashboard'),
    path ('dashboard/categories',views.categories, name = 'categories'),
    path ('dashboard/categories/add',views.add_categories, name = 'add_categories'),
    path ('dashboard/categories/edit/<int:pk>',views.edit_categories, name = 'edit_categories'),
    path ('dashboard/categories/delete/<int:pk>',views.delete_categories, name = 'delete_categories'),
  
]