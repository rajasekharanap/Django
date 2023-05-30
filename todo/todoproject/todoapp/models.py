from django.db import models

class Todo(models.Model):
    name=models.TextField(max_length="200")
    priority=models.IntegerField()
    date=models.DateTimeField()
    def __str__(self):
        return self.name
