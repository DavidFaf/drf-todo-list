# Generated by Django 4.2.1 on 2023-06-04 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_remove_todolist_items_todolist_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='folder',
            field=models.ForeignKey(default='All', on_delete=django.db.models.deletion.CASCADE, to='todo_list.folder'),
        ),
    ]