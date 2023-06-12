from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view()),
    path('<int:pk>/', views.TodoListDetailView.as_view(), name='todolist_detail'),
    path('<int:pk>/update/', views.TodoListUpdateView.as_view()),
    path('<int:pk>/delete/', views.TodoListDeleteView.as_view()),
    path('folder/', views.FolderListView.as_view()),
    path('<int:pk>/folder/', views.FolderDetailView.as_view(), name='folder_detail'),
    path('<int:pk>/folder/update/', views.FolderUpdateView.as_view()),
    path('<int:pk>/folder/delete/', views.FolderDeleteView.as_view()),







    # path('create-list-item/', views.ListItemView.as_view())
]