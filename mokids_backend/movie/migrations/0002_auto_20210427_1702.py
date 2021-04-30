# Generated by Django 3.1.7 on 2021-04-27 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watcheduser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='watched_user',
            field=models.ManyToManyField(related_name='watched_user', through='movie.WatchedUser', to=settings.AUTH_USER_MODEL),
        ),
    ]