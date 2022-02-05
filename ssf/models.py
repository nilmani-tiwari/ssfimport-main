from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

from django.core.validators import FileExtensionValidator
from django.db.models import CASCADE
from django.utils.text import slugify
from django.conf import settings
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
    blog_image = models.ImageField(upload_to='blog_image/', blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)
    published = models.DateField(auto_now_add=True)
    hit_count=models.IntegerField(default=0, blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(BlogPost, self).save(*args, **kwargs)



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
        verbose_name_plural = "3- Videos Categories"



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

class VideoUpload(models.Model):
    
    video_id = models.AutoField(primary_key=True)
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
    record_date = models.CharField(max_length=100,null=True, blank=True)
    
    country = models.CharField(max_length=100, null=True, blank=True)

    hit_count = models.IntegerField( verbose_name="views",default=0,null=True, blank=True)
    rated_by = models.IntegerField(default=0,null=True, blank=True)
    rating = models.FloatField(default=0,null=True, blank=True)
    producer = models.TextField(null=True, blank=True)
    director = models.TextField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True) 
    poster_url = models.URLField(null=True, blank=True) 
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
        verbose_name_plural = "4- Videos"


    @classmethod
    def insert_str(cls,string, str_to_insert, index):
        
        return string[:index] + str_to_insert + string[index:]

    def save(self, *args, **kwargs):
        
        if  self.poster_image and ("uploads/poster/" in str(self.poster_image) ):
            self.poster_url = self.poster_image.url
            
        elif self.poster_image and ("uploads/poster/" not in str(self.poster_image) ):
            self.poster_url = settings.AWS_S3_ENDPOINT_URL+settings.AWS_STORAGE_BUCKET_NAME+"/uploads/poster/"+get_poster_path(VideoUpload,str(self.poster_image),"")
            
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