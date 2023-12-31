# Generated by Django 4.2.4 on 2023-11-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0002_remove_movie_starring_audience_review_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='audience_review',
            name='slug',
            field=models.SlugField(default=models.CharField(blank=True, max_length=50, null=True), unique=True),
        ),
        migrations.AlterField(
            model_name='audience_review',
            name='review',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='ott',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
