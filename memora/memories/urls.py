from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_memory, name='add_memory'),
    path('', views.memory_list, name='memory_list'),
    path('public/', views.public_memories, name='public_memories'),
    path('delete/<int:memory_id>/', views.delete_memory, name='delete_memory'),

]
