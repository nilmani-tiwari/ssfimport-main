# Generated by Django 3.1.7 on 2021-09-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal_payment', '0004_plansubscribeduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='plansubscribeduser',
            name='user_contact',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
