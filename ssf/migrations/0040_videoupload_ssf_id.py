# Generated by Django 3.2 on 2022-07-31 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssf', '0039_auto_20220518_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoupload',
            name='ssf_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
