from django.db import models


class TodoList(models.Model):
    name = models.TextField(max_length=50)
    total = models.IntegerField(default=0)
    completed = models.IntegerField(default=0)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'todo_list'


class Task(models.Model):
    todoList = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    task = models.TextField()
    completed = models.BooleanField(default=False)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'task'
