# Generated by Django 3.0 on 2022-08-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='reservation_id',
            field=models.CharField(max_length=20, verbose_name='予約ID'),
        ),
    ]
