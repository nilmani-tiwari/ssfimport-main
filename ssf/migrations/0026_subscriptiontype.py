# Generated by Django 3.1.1 on 2022-02-11 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssf', '0025_videoupload_home_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Subscription Type',
                'verbose_name_plural': 'Subscription Types',
            },
        ),
    ]
