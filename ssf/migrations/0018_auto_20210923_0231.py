# Generated by Django 3.1.7 on 2021-09-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssf', '0017_videoupload_sub_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, unique=True),
        ),
    ]
