# Generated by Django 3.1.1 on 2022-03-09 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ssf', '0029_auto_20220211_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoupload',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_uploded_video', to=settings.AUTH_USER_MODEL),
        ),
    ]
