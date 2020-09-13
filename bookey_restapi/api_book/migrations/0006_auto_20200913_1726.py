# Generated by Django 3.0.3 on 2020-09-13 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_book', '0005_auto_20200913_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestseller',
            name='bid',
            field=models.ForeignKey(db_column='bid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api_book.Book'),
        ),
    ]
