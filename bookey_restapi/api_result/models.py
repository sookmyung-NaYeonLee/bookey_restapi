from django.db import models

class Result(models.Model):
    bid = models.ForeignKey('api_book.Book', on_delete=models.CASCADE, db_column='bid',primary_key=True)
    good = models.FloatField()

    class Meta:
        db_table = 'Result'