from django.urls import path , include
from . import views


urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('todos/', views.TodoListCreate.as_view()),
    
        
]


