# from curses.ascii import isdigit
from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

from django.core.validators import FileExtensionValidator
from django.db.models import CASCADE, SET_NULL
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid
import os
# Create your models here.

import os
import uuid,random


from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _




class project_image(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __str__(self):
        return self.title+"  "+ self.slug


class project_details(models.Model):
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=200, blank=True, null=True)
    slug = models.CharField(max_length=200, unique=True)
    title_logo_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    
    logo_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    about_logo = models.CharField(max_length=200, blank=True, null=True)

    slider1_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    about_slider1 = models.CharField(max_length=200, blank=True, null=True)

    slider2_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    about_slider2 = models.CharField(max_length=200, blank=True, null=True)

    slider3_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    about_slider3 = models.CharField(max_length=200, blank=True, null=True)

    slider4_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    about_slider4 = models.CharField(max_length=200, blank=True, null=True)

    slider5_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    about_slider5 = models.CharField(max_length=200, blank=True, null=True)
    
    slider5_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    about_slider5 = models.CharField(max_length=200, blank=True, null=True)

    slider6_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    about_slider6 = models.CharField(max_length=200, blank=True, null=True)

    error_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    about_error = models.CharField(max_length=200, blank=True, null=True)

    default_poster_image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    about_default_poster = models.CharField(max_length=200, blank=True, null=True)

    title_logo_url = models.URLField(null=True, blank=True) 
    logo_url = models.URLField(null=True, blank=True) 
    slider1_url = models.URLField(null=True, blank=True) 
    slider2_url = models.URLField(null=True, blank=True) 
    slider3_url = models.URLField(null=True, blank=True) 
    slider4_url = models.URLField(null=True, blank=True) 
    slider5_url = models.URLField(null=True, blank=True) 
    slider6_url = models.URLField(null=True, blank=True) 
    error_url = models.URLField(null=True, blank=True) 
    default_poster_url = models.URLField(null=True, blank=True) 


    desc = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    active = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')


  

    def save(self, *args, **kwargs):
        
        if  self.title_logo_image and ("project_image/" in str(self.title_logo_image) ):
            self.title_logo_url = self.title_logo_image.url
        elif self.title_logo_image and ("project_image/" not in str(self.title_logo_image) ):
            self.title_logo_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.title_logo_image)

        
        if  self.logo_image and ("project_image/" in str(self.logo_image) ):
            self.logo_url = self.logo_image.url
        elif self.logo_image and ("project_image/" not in str(self.logo_image) ):
            self.logo_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.logo_image)

        
        if  self.slider1_image and ("project_image/" in str(self.slider1_image) ):
            self.slider1_url = self.slider1_image.url
        elif self.slider1_image and ("project_image/" not in str(self.slider1_image) ):
            self.slider1_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider1_image)

       
        if  self.slider2_image and ("project_image/" in str(self.slider2_image) ):
            self.slider2_url = self.slider2_image.url
        elif self.slider2_image and ("project_image/" not in str(self.slider2_image) ):
            self.slider2_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider2_image)

        
        if  self.slider3_image and ("project_image/" in str(self.slider3_image) ):
            self.slider3_url = self.slider3_image.url
        elif self.slider3_image and ("project_image/" not in str(self.slider3_image) ):
            self.slider3_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider3_image)

        if  self.slider4_image and ("project_image/" in str(self.slider4_image) ):
            self.slider4_url = self.slider4_image.url
        elif self.slider4_image and ("project_image/" not in str(self.slider4_image) ):
            self.slider4_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider4_image)

        if  self.slider5_image and ("project_image/" in str(self.slider5_image) ):
            self.slider5_url = self.slider5_image.url
        elif self.slider5_image and ("project_image/" not in str(self.slider5_image) ):
            self.slider5_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider5_image)

        #print("project_image" in str(self.slider6_image) ,10000000000000000000000000000000000,type(self.slider6_image),self.slider6_image)
        if  self.error_image and ("project_image/" in str(self.error_image) ):
            self.error_url = self.error_image.url
        elif self.error_image and ("project_image/" not in str(self.error_image) ):
            self.error_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.error_image)

        if  self.slider6_image and ("project_image/" in str(self.slider6_image) ):
            self.slider6_url = self.slider6_image.url
        elif self.slider6_image and ("project_image/" not in str(self.slider6_image) ):
            self.slider6_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider6_image)
        
        if  self.default_poster_image and ("project_image/" in str(self.default_poster_image) ):
            self.default_poster_url = self.default_poster_image.url
        elif self.default_poster_image and ("project_image/" not in str(self.default_poster_image) ):
            self.default_poster_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.default_poster_image)

        if not self.slug:
            self.slug = slugify(self.title)
        return super(project_details, self).save(*args, **kwargs)
    
    def save1(self, *args, **kwargs):
        
        if  self.title_logo_image and ("project_image/" in str(self.title_logo_image) ):
            self.title_logo_url = self.title_logo_image.url
        elif self.title_logo_image and ("project_image/" not in str(self.title_logo_image) ):
            self.title_logo_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.title_logo_image)

        
        if  self.logo_image and ("project_image/" in str(self.logo_image) ):
            self.logo_url = self.logo_image.url
        elif self.logo_image and ("project_image/" not in str(self.logo_image) ):
            self.logo_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.logo_image)

        
        if  self.slider1_image and ("project_image/" in str(self.slider1_image) ):
            self.slider1_url = self.slider1_image.url
        elif self.slider1_image and ("project_image/" not in str(self.slider1_image) ):
            self.slider1_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider1_image)

       
        if  self.slider2_image and ("project_image/" in str(self.slider2_image) ):
            self.slider2_url = self.slider2_image.url
        elif self.slider2_image and ("project_image/" not in str(self.slider2_image) ):
            self.slider2_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider2_image)

        
        if  self.slider3_image and ("project_image/" in str(self.slider3_image) ):
            self.slider3_url = self.slider3_image.url
        elif self.slider3_image and ("project_image/" not in str(self.slider3_image) ):
            self.slider3_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider3_image)

        if  self.slider4_image and ("project_image/" in str(self.slider4_image) ):
            self.slider4_url = self.slider4_image.url
        elif self.slider4_image and ("project_image/" not in str(self.slider4_image) ):
            self.slider4_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider4_image)

        if  self.slider5_image and ("project_image/" in str(self.slider5_image) ):
            self.slider5_url = self.slider5_image.url
        elif self.slider5_image and ("project_image/" not in str(self.slider5_image) ):
            self.slider5_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider5_image)

        #print("project_image" in str(self.slider6_image) ,10000000000000000000000000000000000,type(self.slider6_image),self.slider6_image)
        if  self.error_image and ("project_image/" in str(self.error_image) ):
            self.error_url = self.error_image.url
        elif self.error_image and ("project_image/" not in str(self.error_image) ):
            self.error_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.error_image)

        if  self.slider6_image and ("project_image/" in str(self.slider6_image) ):
            self.slider6_url = self.slider6_image.url
        elif self.slider6_image and ("project_image/" not in str(self.slider6_image) ):
            self.slider6_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.slider6_image)

        if  self.default_poster_image and ("project_image/" in str(self.default_poster_image) ):
            self.default_poster_url = self.default_poster_image.url
        elif self.default_poster_image and ("project_image/" not in str(self.default_poster_image) ):
            self.default_poster_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/project_image/"+str(self.default_poster_image)

        
        if not self.slug:
            self.slug = slugify(self.title)
        return super(project_details, self).save1(*args, **kwargs)

 


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content=RichTextField(blank=True,null=True)
    blog_image = models.ImageField(upload_to='blog_image/', blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)
    author=models.CharField(max_length=100, blank=True, null=True)
    published = models.DateField(auto_now_add=True)
    hit_count=models.IntegerField(default=0, blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(BlogPost, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "VideoCategory"
        verbose_name_plural = "4- Blog Post"


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/VideoUpload', filename)



import datetime
def get_video_path(instance, filename,upload_path='uploads/VideoUpload'):
    time=datetime.datetime.now()
    timestamp=datetime.datetime.strftime(time,"%d-%b-%y-%H_%M_%S")
    file=filename.split('.')
    new_string=""
    ext = file[-1]
    file.pop()
    input_string="".join(file)
    for i in input_string:
        if i.isupper():
            new_string+=i.upper()
        if (i.isdigit()):
            new_string+=i.upper()
        if i=="_":
            new_string+=i.upper()
        
        if i.islower():
            new_string+=i.upper()
            
    new_filename=    new_string+"_"+timestamp

    filename=new_filename+"."+ext
    return os.path.join(upload_path, filename)

def get_poster_path(instance, filename,upload_path='uploads/poster'):
    time=datetime.datetime.now()
    timestamp=datetime.datetime.strftime(time,"%d-%b-%y-%H_%M_%S")
    file=filename.split('.')
    new_string=""
    ext = file[-1]
    file.pop()
    input_string="".join(file)
    for i in input_string:
        if i.isupper():
            new_string+=i.upper()
        if (i.isdigit()):
            new_string+=i.upper()
        if i=="_":
            new_string+=i.upper()
        if i.islower():
            new_string+=i.upper()
            
    new_filename=    new_string+"_"+timestamp

    filename=new_filename+"."+ext
    return os.path.join(upload_path, filename)


class VideoCategory(models.Model):  #Category
    category_id = models.AutoField(primary_key=True)
    slug = models.SlugField(unique=True, max_length=500,null=True)
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.category_id} Cat: {self.category_name}"

    class Meta:
        verbose_name = "VideoCategory"
        verbose_name_plural = "1- Videos Categories"



class VideoSubCategory(models.Model):  #Category
    subcategory_id = models.AutoField(primary_key=True)
    slug = models.SlugField(unique=True, max_length=500,null=True)
    sub_cat = models.ForeignKey('VideoCategory', related_name='VideoSubCategory', on_delete=CASCADE)
    subcategory_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.subcategory_id} Cat: {self.subcategory_name}"

    class Meta:
        verbose_name = "VideoSubCategory"
        verbose_name_plural = "2- Videos Sub Categories"

#VideoUpload(user=user,ssf_id=ssf_id,title=title)
class VideoUpload(models.Model):
    user = models.ForeignKey(User, related_name='user_uploded_video', on_delete=CASCADE,null=True, blank=True)
    video_id = models.AutoField(primary_key=True)
    ssf_id = models.IntegerField(default=0,null=True, blank=True)  
    vendor_id = models.IntegerField(default=0,null=True, blank=True)                   
    title = models.CharField(max_length=500)
    video = models.FileField(upload_to=get_video_path,null=True,
                        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv','flv'])],
                        blank=True,
                        verbose_name=(u'Video content'))
    slug = models.SlugField(unique=True, max_length=500,blank=True)
    video_cat = models.ForeignKey('VideoCategory', related_name='VideoCategory', on_delete=CASCADE)
    sub_cat = models.ForeignKey('VideoSubCategory', related_name='VideoSubCategory', on_delete=CASCADE, blank=True, null=True)
    poster_image = models.ImageField(upload_to=get_poster_path, blank=True, null=True)
    desc = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    duration = models.FloatField(default=0,null=True, blank=True)
    duration_str=models.CharField(max_length=100,null=True, blank=True)
    record_date = models.CharField(max_length=100,null=True, blank=True)
    
    country = models.CharField(max_length=100, null=True, blank=True)

    hit_count = models.IntegerField( verbose_name="views",default=0,null=True, blank=True)
    rated_by = models.IntegerField(default=0,null=True, blank=True)
    rating = models.FloatField(default=0,null=True, blank=True)
    producer = models.TextField(null=True, blank=True)
    director = models.TextField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True) 
    poster_url = models.URLField(null=True, blank=True) 

    ssf_poster_url = models.URLField(null=True, blank=True) 
    ssf_video_url = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)
    
    active = models.BooleanField(default=True)
    home_active = models.BooleanField(default=True)
    # hit_count=models.IntegerField(default=0, blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    def __str__(self):
        return f"{self.video_id} {self.title} "
    
    class Meta:
        db_table = 'VideoUpload'
        verbose_name = "Video"
        verbose_name_plural = "3- Videos"


    @classmethod
    def insert_str(cls,string, str_to_insert, index):
        
        return string[:index] + str_to_insert + string[index:]

    def save(self, *args, **kwargs):
        
        if  self.poster_image and ("uploads/poster/" in str(self.poster_image) ):
            self.poster_url = self.poster_image.url
            
        elif self.poster_image and ("uploads/poster/" not in str(self.poster_image) ):
            self.poster_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/uploads/poster/"+    str(self.poster_image.url)
            
        if  self.video and ("uploads/VideoUpload/" in str(self.video) ):
            self.video_url = self.video.url
            #print(get_video_path(VideoUpload,str(self.video),""),1)
        elif self.video and ("uploads/VideoUpload/" not in str(self.video) ):
            self.video_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/uploads/VideoUpload/"+get_video_path(VideoUpload,str(self.video),"")
            #print(get_video_path(VideoUpload,str(self.video),""),2)

        # if self.video!="":
        #     # settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+str(self.video)
        #     self.video_url=self.video.url
        # if self.poster_url!="":
        #     self.poster_url=self.poster_image.url
        if  self.slug =="":
            string=f"{self.title}{self.desc}{self.keywords}{self.active}".split()
            random.shuffle(string)
            string="-".join(string)
            self.slug = slugify(string)
        return super(VideoUpload, self).save(*args, **kwargs)




# class Model1(models.Model):
#     First = models.IntegerField(default=0)
#     Second = models.IntegerField(default=0)
#     Auto_Sum = models.IntegerField(default=0)

#     def save(self, *args, **kwargs):
        
#         if True:

#             self.Auto_Sum=self.First+self.Second
        
#         return super(Model1, self).save(*args, **kwargs)

    


# These two auto-delete files from filesystem when they are unneeded:

# @receiver(models.signals.post_delete, sender=VideoUpload)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` object is deleted.
#     """
#     if instance.video:
#         if os.path.isfile(instance.video.path):
#             os.remove(instance.video.path)

# @receiver(models.signals.pre_save, sender=VideoUpload)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `MediaFile` object is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False

#     try:
#         old_file = VideoUpload.objects.get(pk=instance.pk).video
#     except VideoUpload.DoesNotExist:
#         return False

#     new_file = instance.video
#     if not old_file == new_file:
#         #if os.path.isfile(old_file.path):
#         os.remove(old_file.path)



class SubscriptionType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __str__(self):
        return f"[SubscritionType: {self.id}] {self.name}"

    class Meta:
        verbose_name = "Subscription Type"
        verbose_name_plural = "5- Subscription Types"



class EmailSubscription(models.Model):
    user = models.ForeignKey(User, related_name='subscriber', on_delete=CASCADE)
    subscription_type = models.ForeignKey('SubscriptionType', related_name='subscription_type', on_delete=SET_NULL, null=True, blank=True)
    subscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __str__(self):
        return f" {self.id}] {self.user} <-> {self.subscription_type.name}"

    class Meta:
        verbose_name = "Email Subscription"
        verbose_name_plural = "6- Email Subscriptions"



    @staticmethod
    def user_upload(type, email_ids=None):

        # email_ids =['parag@tickle.life', 'a@a.com', 'sevenaces@gmail.com']

        existing_users = User.objects.filter(email__in=email_ids).values_list('email', flat=True)
        userslist = []
        for email in email_ids:
            u = User.objects.filter(email=email)
            if u.exists():
                userslist.append(u.first())
            else:
                u = User.objects.create(username=email, email=email)
                userslist.append(u)



        for user in userslist:
            EmailSubscription.objects.get_or_create(subscription_type=type, user=user)

        return

class UserFavoriteVideo(models.Model):
    CHOICESs=( ("video","video"),("blog","blog"))
    CHOICES=( ("like","like"),("dislike","dislike"))

    subscriber = models.ForeignKey('EmailSubscription', related_name='sub_fav_s', on_delete=CASCADE)
    content_type = models.CharField(max_length=50, choices=CHOICESs, default='video',blank=True, null=True)
    content_id = models.IntegerField(blank=True, null=True)

    label = models.CharField(max_length=50, choices=CHOICES,blank=True, null=True)
    fab=models.BooleanField(default=False)
    subscribed = models.BooleanField(default=False)
    # like=models.PositiveBigIntegerField(default=0)
    # dislike=models.PositiveBigIntegerField(default=0)
    # fabrate=models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __str__(self):
        return f"{self.subscriber} (favs) {self.label}"

    class Meta:
        verbose_name = "User Favorite"
        verbose_name_plural = "7- User Favorite Videos"


class UserComment(models.Model):
    CHOICESs=( ("video","video"),("blog","blog"))
    subscriber = models.ForeignKey('EmailSubscription', related_name='vid_com_s', on_delete=CASCADE)

    content_type = models.CharField(max_length=50, choices=CHOICESs, default='video',blank=True, null=True)
    content_id = models.IntegerField(blank=True, null=True)

    comment = models.TextField(default='This is very nice.',blank=True, null=True)
    home_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __str__(self):
        return f"{self.subscriber} comment on {self.content_type}"

    class Meta:
        verbose_name = "Video Comment"
        verbose_name_plural = "8- Video Comments"


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=100,blank=True, null=True)
    desc=models.TextField(max_length=2000,blank=True, null=True)
    password = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    image_url = models.URLField(null=True, blank=True) 

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __str__(self):
        return f"{self.user}  {self.email}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "9- User Profile"

class UserContactMessage(models.Model):
    user = models.ForeignKey(User, related_name='user_contact_us', on_delete=CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=100,blank=True, null=True)
    subject = models.CharField(max_length=100,blank=True, null=True)
    message=models.TextField(max_length=2000,blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    # def __str__(self):
    #     return f"{self.user}  {self.email}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "10- User Contact Us Message"


# class VideoBlogSubscription(models.Model):
#     CHOICESs=( ("video","video"),("blog","blog"))
#     user = models.ForeignKey(User, related_name='video_blog_subscriber', on_delete=CASCADE)
#     content_type = models.CharField(max_length=50, choices=CHOICESs, default='video',blank=True, null=True)
#     content_id = models.IntegerField(blank=True, null=True)

#     subscribed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)
