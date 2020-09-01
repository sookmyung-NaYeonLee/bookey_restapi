from django.db import models

# Create your models here.
class AppUser(models.Model):
    uid = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'AppUser'