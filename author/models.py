from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    Bio = models.TextField()
    phone_no = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        