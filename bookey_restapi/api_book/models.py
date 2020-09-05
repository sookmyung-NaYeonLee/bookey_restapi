from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=30, null=False)
    author = models.CharField(max_length=50, null=False)
    publisher = models.CharField(max_length=30, null=False)
    price = models.CharField(max_length=20, null=False)
    list = models.TextField(null=False)
    description = models.TextField(null=False)
    pages = models.CharField(max_length=20, null=False)
    img_url = models.TextField(null=False)

    class Meta:
        db_table = "Book"

