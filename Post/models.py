from django.db import models
from author.models import Author
from Category.models import category
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    categori = models.ManyToManyField(category)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title