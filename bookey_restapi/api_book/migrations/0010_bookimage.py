# Generated by Django 3.0.3 on 2020-09-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_book', '0009_auto_20200914_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'BookImage',
            },
        ),
    ]
