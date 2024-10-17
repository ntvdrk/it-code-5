from django.db import models

# Create your models here.
class store(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)

    def str(self):
        return self.name

