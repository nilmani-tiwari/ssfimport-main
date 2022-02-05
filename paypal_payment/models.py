from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models import CASCADE
from datetime import datetime,date
import random
# Create your models here.


class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=100,blank=True)
    access_time_from = models.DateTimeField()
    access_time_to = models.DateTimeField()
    price = models.FloatField(default=0)

    sort_order = models.IntegerField(default=0)
  
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)
    active = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.description}"

    def save(self, *args, **kwargs):
        if  self.slug=="":
            string=f"{self.title}{self.description}{self.price}{self.active}".split()
            random.shuffle(string)
            string="-".join(string)
            self.slug = slugify(string)
        return super(Plan, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Subscription Plan"
        verbose_name_plural = "1-  Subscription Plan"



# class subscribed_user(models.Model):
#     plan_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     slug = models.SlugField(unique=True, max_length=100,blank=True)
#     access_time_from = models.DateTimeField()
#     access_time_to = models.DateTimeField()
#     price = models.FloatField(default=0)


class PlanSubscribedUser(models.Model):
    subscribed_id = models.AutoField(primary_key=True)
    plan= models.ForeignKey('plan', related_name='plan', on_delete=CASCADE)
    user= models.IntegerField(default=0,null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    user_contact = models.CharField(max_length=25,  blank=True, null=True)
    pwd = models.CharField(max_length=100, null=True, blank=True)
    amount = models.FloatField(default=0)
    subscribed_date=models.DateTimeField(default=datetime.now)
    expiry_date=models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    # subs_user_id=models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "PlanSubscribedUser"
        verbose_name_plural = "2- Subscribed User"



class ViewPlan(models.Model):
    view_id = models.AutoField(primary_key=True)
    video= models.IntegerField(default=0,null=True, blank=True)
    user= models.IntegerField(default=0,null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    user_contact = models.CharField(max_length=25,  blank=True, null=True)
    pwd = models.CharField(max_length=100, null=True, blank=True)
    amount = models.FloatField(default=0)
    subscribed_date=models.DateTimeField(default=datetime.now)
    expiry_date=models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    # subs_user_id=models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "ViewPlan"
        verbose_name_plural = "3- Pay Per View User"

class s3control(models.Model):
    s3_id=models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.s3_id}"
