# Generated by Django 3.2 on 2022-05-14 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal_payment', '0009_viewplan_log_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='plansubscribeduser',
            name='log_status',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
