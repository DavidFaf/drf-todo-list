from django.contrib import admin
from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple

# Register your models here.


from .models import *

myModels = [TodoList, Folder, ListItem]  # iterable list

admin.site.register(myModels)