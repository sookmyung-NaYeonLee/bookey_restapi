# Generated by Django 3.0.3 on 2020-09-21 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_book', '0010_bookimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookImage',
        ),
    ]