# Generated by Django 3.1.7 on 2021-09-22 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal_payment', '0007_s3control'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plansubscribeduser',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='viewplan',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
