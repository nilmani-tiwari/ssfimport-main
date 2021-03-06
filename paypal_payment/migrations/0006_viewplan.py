# Generated by Django 3.1.7 on 2021-09-22 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal_payment', '0005_plansubscribeduser_user_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewPlan',
            fields=[
                ('view_id', models.AutoField(primary_key=True, serialize=False)),
                ('video', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('user_contact', models.CharField(blank=True, max_length=25, null=True)),
                ('pwd', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.FloatField(default=0)),
                ('subscribed_date', models.DateTimeField(default=datetime.datetime.now)),
                ('expiry_date', models.DateTimeField()),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'ViewPlan',
                'verbose_name_plural': '3- Pay Per View User',
            },
        ),
    ]
