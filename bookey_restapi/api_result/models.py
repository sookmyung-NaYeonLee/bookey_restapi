from django.db import models

class Result(models.Model):
    bid = models.ForeignKey('api_book.Book', on_delete=models.CASCADE, db_column='bid')
    good = models.CharField(max_length=10)

    class Meta:
        db_table = 'Result'