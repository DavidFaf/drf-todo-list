from django.db import models
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class ListItem(models.Model):
    title = models.CharField(blank=False, max_length=120)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.title

    def is_completed(self) -> bool:
        return self.completed

class Folder(models.Model):
    title = models.CharField(max_length=120)

    
    def __str__(self) -> str:
        return self.title

class TodoList(models.Model):
    # folder_name = 
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=120, default="New To-do List")
    date_updated = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(ListItem, blank=True)  # related_name='TodoLists'
    folder = models.ForeignKey(Folder, default=1 ,on_delete=models.CASCADE, related_name='todo_lists')

    @property
    def endpoint(self):
        return reverse('todolist_detail', kwargs={'pk':self.pk})
    
    @property
    def path(self):
        return f'/lists/{self.pk}'


