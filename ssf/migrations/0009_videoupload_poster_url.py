# Generated by Django 3.1.7 on 2021-09-02 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssf', '0008_auto_20210902_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoupload',
            name='poster_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
