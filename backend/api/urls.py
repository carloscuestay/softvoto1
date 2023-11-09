from django.urls import path
from . import views
from api.views import signup


urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('todos/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),
    path('signup/', views.TodoToggleComplete.as_view(), name='signup'),
]


