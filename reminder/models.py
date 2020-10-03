from django.db import models


class Reminder(models.Model):
    title = models.TextField()
    description = models.TextField()
    dateTime = models.DateTimeField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reminder'
