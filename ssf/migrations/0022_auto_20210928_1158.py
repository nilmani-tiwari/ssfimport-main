# Generated by Django 3.1.7 on 2021-09-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssf', '0021_auto_20210928_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]
