# Generated by Django 4.2.3 on 2023-07-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Watchlist', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]