from django.db import models

class Bookshelf(models.Model):
    uid = models.ForeignKey('api_user.AppUser', on_delete=models.CASCADE, db_column='uid')
    bid = models.ForeignKey('api_book.Book', on_delete=models.PROTECT, db_column='bid')
    review = models.TextField()

    class Meta:
        db_table = 'Bookshelf'