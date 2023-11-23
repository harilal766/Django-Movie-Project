# Generated by Django 4.2.3 on 2023-07-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='starring',
        ),
        migrations.AddField(
            model_name='audience_review',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audience_review',
            name='review',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
    ]