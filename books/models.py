from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.CharField(max_length=13)

    def self_title(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk":self.pk})