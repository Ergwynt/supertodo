from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)
    slug = models.SlugField(max_length=150, default='')
    complete_before = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
