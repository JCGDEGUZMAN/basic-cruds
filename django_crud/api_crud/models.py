from django.db import models

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subjects'

    def __str__ (self):
        return self.title