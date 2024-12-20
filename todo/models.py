from django.db import models
from user.models import UserModel
# Create your models here.


class TodoModel(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    status = models.BooleanField(default=False)
    cron = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name="tasks")


    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "todos"
        verbose_name = "todo"
        verbose_name_plural = "todos"
        ordering = ['-created_at']


