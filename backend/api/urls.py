from django.urls import path
from . import views


urlpatterns = [
    path('', views.TodoList.as_view()),
    path('todos/', views.TodoList.as_view()),
    path('todos/', views.TodoListCreate.as_view()),
    
        
]


