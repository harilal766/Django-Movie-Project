# Generated by Django 4.2.3 on 2023-07-19 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Crew', '0001_initial'),
        ('Details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('year', models.CharField(blank=True, max_length=5)),
                ('language', models.CharField(blank=True, max_length=50)),
                ('release', models.CharField(blank=True, max_length=100)),
                ('rating', models.CharField(blank=True, max_length=20)),
                ('poster', models.ImageField(blank=True, upload_to='movies/poster')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='movies/cover')),
                ('duration', models.CharField(blank=True, default=None, max_length=50)),
                ('ott', models.TextField(blank=True, max_length=50, null=True)),
                ('based', models.CharField(blank=True, max_length=100, null=True)),
                ('synopsis', models.TextField(blank=True, max_length=1000)),
                ('trailer', models.CharField(blank=True, max_length=500)),
                ('Characters', models.ManyToManyField(blank=True, related_name='character', to='Crew.character')),
                ('actors', models.ManyToManyField(blank=True, related_name='actor', to='Crew.actor')),
                ('certification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Details.certification')),
                ('cinematographer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Crew.cinematographer')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Crew.director')),
                ('genres', models.ManyToManyField(blank=True, to='Details.genre')),
                ('starring', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actors', to='Crew.actor')),
                ('streaming', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Details.streaming')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('writers', models.ManyToManyField(blank=True, related_name='writer', to='Crew.writer')),
            ],
        ),
        migrations.CreateModel(
            name='Audience_Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('review', models.TextField(blank=True, max_length=3000, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.movie')),
                ('user', models.ForeignKey(default='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]