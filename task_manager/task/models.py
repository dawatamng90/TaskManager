from django.db import models
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed_on_time', 'Completed On Time'),
        ('completed_after_time', 'Completed After Time'),
    ]

    task_name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task_name

    def save(self, *args, **kwargs):
        if self.completed_date:
            if self.completed_date <= self.due_date:
                self.status = 'completed_on_time'
            else:
                self.status = 'completed_after_time'
        else:
            self.status = 'pending'
        super().save(*args, **kwargs)


    def update_completion_status(self):
        """Updates the task's status based on the completion date."""
        if self.completed_date:
            if self.completed_date <= self.due_date:
                self.status = 'completed_on_time'
            else:
                self.status = 'completed_after_time'
        else:
            self.status = 'pending'
        self.save()