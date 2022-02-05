import pdb
import time
from django.contrib.auth.models import User
from datetime import datetime
import csv

from django.db import models
from datetime import datetime
default=datetime.now
from django.utils.html import format_html
# Create your models here.
import uuid
import os

from django.conf import settings
from django.db import models
import html

# Create your models here.
from django.db.models import CASCADE
from django.utils.text import slugify

from localwp.models import *
from ssftemp.utils import get_ssf_db

# from ssfimport.utils.wputils import wp_content_processor
# import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)



def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/logos', filename)




class Video(models.Model):
    ssf_id = models.AutoField(primary_key=True)
    vendor_id = models.IntegerField()                   
    title = models.CharField(max_length=500)
    desc = models.TextField(null=True, blank=True)
    featured_desc = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    duration = models.FloatField(null=0)
    record_date = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    original_format = models.CharField(max_length=100, null=True, blank=True)
    views = models.IntegerField()
    rated_by = models.IntegerField()
    rating = models.FloatField()
    producer = models.TextField(null=True, blank=True)
    director = models.TextField(null=True, blank=True)
    consultant = models.TextField(null=True, blank=True)
    quote = models.TextField(null=True, blank=True)
    quote_author = models.TextField(null=True, blank=True)
    quote_location = models.CharField(max_length=100, null=True, blank=True)
    # video_id=models.AutoField(primary_key=True)
    video = models.FileField(upload_to=get_file_path,
                        null=True,
                        blank=True,
                        verbose_name=(u'Video content'))
    video_url = models.URLField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __str__(self):
        return f"{self.title} / {self.ssf_id}"

    def get_video_url(self):
        return f"{settings.VIDEO_BASE}{self.ssf_id}_1800.mp4"

    class Meta:
        db_table = 'video'
        verbose_name = "Video"
        verbose_name_plural = "4- Videos"

    @staticmethod
    def populate(size=100):

        db = get_ssf_db()
        cursor = db.cursor()

        length = cursor.execute("SELECT COUNT(*) FROM video")
        length = cursor.fetchone()[0]

        for i in range(int(length / size) + 1):
            cursor.execute(f"SELECT * FROM video LIMIT {i * size}, {size}")
            data = cursor.fetchall()
            for video in data:

                if not Video.objects.filter(ssf_id=video[0]).exists():
                    print(f"Processing {video[0]} [{video[3]}]")

                    Video.objects.create(
                        ssf_id=video[0],
                        vendor_id=video[2],
                        title=html.unescape(video[3]),
                        desc=html.unescape(video[4]),
                        featured_desc=html.unescape(video[5]),
                        keywords=video[6],
                        duration=video[12],
                        record_date=video[17],
                        city=video[18],
                        country=video[19],
                        original_format=video[20],
                        views=video[22],
                        rated_by=video[27],
                        rating=video[28],
                        producer=video[35],
                        director=video[36],
                        consultant=video[37],
                        quote=html.unescape(video[38]),
                        quote_author=video[39],
                        quote_location=video[40]
                    )

        db.close()

        return

    def refresh(self):

        db = get_ssf_db()
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM video where VID={self.ssf_id} LIMIT 1")
        video = cursor.fetchone()

        Video.objects.filter(id=self.id).update(
            ssf_id=video[0],
            vendor_id=video[2],
            title=html.unescape(video[3]),
            desc=html.unescape(video[4]),
            featured_desc=html.unescape(video[5]),
            keywords=video[6],
            duration=video[12],
            record_date=video[17],
            city=video[18],
            country=video[19],
            original_format=video[20],
            views=video[22],
            rated_by=video[27],
            rating=video[28],
            producer=video[35],
            director=video[36],
            consultant=video[37],
            quote=html.unescape(video[38]),
            quote_author=video[39],
            quote_location=video[40]
        )
        db.close()
        return

    @staticmethod
    def write_all_to_wp(only_thumb=False):
        videos = Video.objects.all()
        c = videos.count()
        i = 1
        for video in videos:
            print(f'[PROCESSING VIDEO] {i}/{c} [{video}]')
            i += 1
            if not only_thumb:
                video.write_to_wp()
            video.update_thumb()
        return

    def write_to_wp(self):
        old = WpPosts.objects.using('wp').filter(guid=f"{settings.VIDEO_BASE}{self.ssf_id}")
        if not old.exists():
            if self.record_date == '0000-00-00':
                rd = datetime.utcnow()
            else:
                rd = datetime.strptime(self.record_date, '%Y-%m-%d')
            post = WpPosts.objects.using('wp').create(
                post_author=1,
                post_date=rd,
                post_date_gmt=rd,
                post_modified=rd,
                post_modified_gmt=rd,
                post_content=self.desc,
                post_excerpt=self.desc,
                post_title=self.title,
                post_status='publish',
                comment_status='open',
                ping_status='closed',
                post_name=slugify(self.title),
                post_type='video_skrn',
                guid=f'{settings.VIDEO_BASE}{self.ssf_id}',
                post_parent=0,
                menu_order=0,
                comment_count=0
            )
            WpPostmeta.objects.using('wp').create(
                post_id=post.id,
                meta_key='progression_studios_video_post',
                meta_value=f'{settings.VIDEO_BASE}{self.ssf_id}_1800.mp4'
            )
            WpPostmeta.objects.using('wp').create(
                post_id=post.id,
                meta_key='_average_ratings',
                meta_value=self.rating*2
            )

            self.create_vod()

        return

    def create_vod(self):
        wp_post = WpPosts.objects.using('wp').filter(guid=f"{settings.VIDEO_BASE}{self.ssf_id}").first()

        WpPostmeta.objects.using('wp').create(
            post_id=wp_post.id,
            meta_key='arm_is_paid_post',
            meta_value=1
        )

        WpArmSubscriptionPlans.objects.using('wp').create(
            arm_subscription_plan_name=self.title,
            arm_subscription_plan_description='',
            arm_subscription_plan_type='paid_finite',
            arm_subscription_plan_options='a:10:{s:9:"pricetext";s:' + str(len(self.title)) +':"' + self.title + '";s:11:"access_type";s:6:"finite";s:12:"payment_type";s:8:"one_time";s:11:"expiry_type";s:18:"joined_date_expiry";s:4:"eopa";a:5:{s:4:"days";s:1:"1";s:5:"weeks";s:1:"1";s:6:"months";s:1:"1";s:5:"years";s:1:"1";s:4:"type";s:1:"D";}s:11:"expiry_date";s:19:"2021-05-02 23:59:59";s:3:"eot";s:5:"block";s:12:"grace_period";a:2:{s:11:"end_of_term";i:0;s:14:"failed_payment";i:0;}s:14:"upgrade_action";s:9:"immediate";s:16:"downgrade_action";s:9:"on_expire";}',
            arm_subscription_plan_amount=0.99,
            arm_subscription_plan_status=1,
            arm_subscription_plan_role='armember',
            arm_subscription_plan_post_id=wp_post.id,
            arm_subscription_plan_is_delete=0,
            arm_subscription_plan_created_date=datetime.utcnow()
        )
        return

    def update_thumb(self):
        post = WpPosts.objects.using('wp').filter(guid=f"{settings.VIDEO_BASE}{self.ssf_id}").first()

        WpPostmeta.objects.using('wp').create(
            post_id=post.id,
            meta_key='progression_studios_poster_image',
            meta_value=f'{settings.THUMB_BASE}{self.ssf_id}.jpg'
        )

        WpPostmeta.objects.using('wp').create(
            post_id=post.id,
            meta_key='progression_studios_header_image',
            meta_value=f'{settings.THUMB_BASE}{self.ssf_id}.jpg'
        )

        WpPostmeta.objects.using('wp').create(
            post_id=post.id,
            meta_key='progression_studios_video_embed_poster',
            meta_value=f'{settings.THUMB_BASE}{self.ssf_id}.jpg'
        )

        WpPostmeta.objects.using('wp').create(
            post_id=post.id,
            meta_key='fifu_image_url',
            meta_value=f'{settings.THUMB_BASE}{self.ssf_id}.jpg'
        )

        WpPostmeta.objects.using('wp').create(
            post_id=post.id,
            meta_key='fifu_image_alt',
            meta_value=self.title,
        )

        rd = datetime.utcnow()
        thumb = WpPosts.objects.using('wp').create(
            post_author=1,
            post_date=rd,
            post_date_gmt=rd,
            post_modified=rd,
            post_modified_gmt=rd,
            post_content=self.desc,
            post_excerpt=self.desc,
            post_title=self.title,
            post_status='publish',
            comment_status='open',
            ping_status='closed',
            post_name=slugify(self.title),
            post_type='attachment',
            guid=f'{settings.THUMB_BASE}{self.ssf_id}.jpg',
            post_parent=post.id,
            menu_order=0,
            comment_count=0,
            post_mime_type='image/jpeg'
        )

        WpPostmeta.objects.using('wp').create(
            post_id=post.id,
            meta_key='_thumbnail_id',
            meta_value=thumb.id,
        )


class VideoCategory(models.Model):  #Category
    ssf_id = models.IntegerField()
    name = models.CharField(max_length=100)
    parent = models.IntegerField(default=0)
    desc = models.TextField(null=True, blank=True)
    video_cat_id=models.AutoField(primary_key=True)

    def __str__(self):
        return f"Cat: {self.name}"

    class Meta:
        verbose_name = "VideoCategory"
        verbose_name_plural = "5- Videos Categories"

    @staticmethod
    def populate():

        db = get_ssf_db()
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM categories")
        data = cursor.fetchall()
        for category in data:

            if not VideoCategory.objects.filter(ssf_id=category[0]).exists():
                print(f"Processing {category[0]} [{category[1]}]")

                VideoCategory.objects.create(
                    ssf_id=category[0],
                    name=category[1],
                    parent=category[2],
                    desc=html.unescape(category[3])
                )

        db.close()

        return

    def refresh(self):

        db = get_ssf_db()
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM categories where id={self.ssf_id}")
        category = cursor.fetchone()
        VideoCategory.objects.filter(ssf_id=self.ssf_id).update(
            name=category[1],
            parent=category[2],
            desc=html.unescape(category[3])
        )

        db.close()

        return

    @staticmethod
    def write_all_to_wp():

        menu_term, c = WpTerms.objects.using('wp').get_or_create(
            name='lib_menu',
            slug='lib_menu',
            term_group=0
        )

        menu_tax, c = WpTermTaxonomy.objects.using('wp').get_or_create(
            term_id = menu_term.term_id,
            taxonomy='nav_menu',
            parent=0,
            count=0
        )

        menu_order = 1
        for cat in VideoCategory.objects.filter(parent=0).order_by('parent'):
            cat.write_to_wp(menu_order)
            for subcat in VideoCategory.objects.filter(parent=cat.ssf_id).order_by('id'):
                subcat.write_to_wp(menu_order, parent=cat.name)
                menu_order += 1
        return

    def write_to_wp(self, menu_order, parent=None):

        print(
            f"self: {self}\nmenu_order: {menu_order}\nparent: {parent}"
        )
        old = WpTerms.objects.using('wp').filter(slug=slugify(self.name))
        if not old.exists():
            term, c = WpTerms.objects.using('wp').get_or_create(
                name=self.name,
                slug=slugify(self.name),
                term_group=0
            )
            WpTermTaxonomy.objects.using('wp').get_or_create(
                term_id=term.term_id,
                taxonomy='video-type' if self.parent == 0 else 'video-category',
                description=self.desc,
                parent=0,
                count=0
            )

        old_post = WpPosts.objects.using('wp').filter(
            post_status='publish',
            post_name=slugify(self.name),
            post_type='page'
        )
        if old_post.exists():
            post = old_post.first()
        else:
            post = WpPosts.objects.using('wp').create(
                post_author=1,
                post_date=datetime.utcnow(),
                post_date_gmt=datetime.utcnow(),
                post_content=f"{self.name} - {self.desc}",
                post_title=f"Videos on {self.name}",
                post_excerpt=f"{self.desc}",
                post_status='publish',
                comment_status='closed',
                ping_status='closed',
                post_password='',
                post_name=slugify(self.name),
                to_ping='',
                pinged='',
                post_modified=datetime.utcnow(),
                post_modified_gmt=datetime.utcnow(),
                post_content_filtered='',
                post_parent=0,
                guid=f'ssf-video-cat-{slugify(self.name)}',
                menu_order=0,
                post_type='page',
                post_mime_type='',
                comment_count=0
            )

        menu_item = WpPosts.objects.using('wp').create(
            post_author=1,
            post_date=datetime.utcnow(),
            post_date_gmt=datetime.utcnow(),
            post_content='',
            post_title=self.name,
            post_excerpt='',
            post_status='publish',
            comment_status='closed',
            ping_status='closed',
            post_password='',
            post_name=f'menu_for_{slugify(self.name)}',
            to_ping='',
            pinged='',
            post_modified=datetime.utcnow(),
            post_modified_gmt=datetime.utcnow(),
            post_content_filtered='',
            post_parent=0,
            guid=f'ssf-video-cat-{slugify(self.name)}',
            menu_order=menu_order,
            post_type='nav_menu_item',
            post_mime_type='',
            comment_count=0
        )
        menu_item.post_name = menu_item.id
        menu_item.guid = f"{settings.WORDPRESS_BASE}?p={menu_item.id}"
        menu_item.save()

        menu_tax = WpTermTaxonomy.objects.using('wp').get(
            term_id=WpTerms.objects.using('wp').get(slug='lib_menu').term_id,
            taxonomy='nav_menu'
        )

        WpTermRelationships.objects.using('wp').create(
            object_id=menu_item.id,
            term_taxonomy_id=menu_tax.term_taxonomy_id,
            term_order=0
        )

        WpPostmeta.objects.using('wp').create(
            post_id=menu_item.id,
            meta_key='_menu_item_type',
            meta_value='post_type'
        )

        WpPostmeta.objects.using('wp').create(
            post_id=menu_item.id,
            meta_key='_menu_item_menu_item_parent',
            meta_value=WpPosts.objects.using('wp').filter(post_title=parent, post_status='publish', post_type='nav_menu_item').first().id if parent else 0
        )

        WpPostmeta.objects.using('wp').create(
            post_id=menu_item.id,
            meta_key='_menu_item_object_id',
            meta_value=WpPosts.objects.using('wp').filter(post_name=slugify(self.name), post_status='publish', post_type='page').first().id
        )

        WpPostmeta.objects.using('wp').create(
            post_id=menu_item.id,
            meta_key='_menu_item_object',
            meta_value='page'
        )

        print("*"*300)


        return


class VideoCategoryMapping(models.Model):
    video = models.ForeignKey('Video', related_name='video_category_v', on_delete=CASCADE)
    category = models.ForeignKey('VideoCategory', related_name='video_category_c', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)
    # video_cat_map_id=models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.video} <=> {self.category}"

    class Meta:
        verbose_name = "Video Category Map"
        verbose_name_plural = "6 Video Category Mapping"

    @staticmethod
    def populate(size=100):

        db = get_ssf_db()
        cursor = db.cursor()

        length = cursor.execute("SELECT COUNT(*) FROM video_cat_relation")
        length = cursor.fetchone()[0]

        VideoCategoryMapping.objects.all().delete()

        for i in range(int(length / size) + 1):
            cursor.execute(f"SELECT * FROM video_cat_relation LIMIT {i * size}, {size}")
            data = cursor.fetchall()
            for map in data:
                if Video.objects.filter(ssf_id=map[1]).exists() and VideoCategory.objects.filter(ssf_id=map[0]).exists():
                    VideoCategoryMapping.objects.create(
                        video=Video.objects.get(ssf_id=map[1]),
                        category=VideoCategory.objects.get(ssf_id=map[0]),
                    )

        db.close()
        return

    @staticmethod
    def write_all_to_wp():
        for vc in VideoCategoryMapping.objects.all():
            vc.write_to_wp()
        return

    def write_to_wp(self):

        video_post = WpPosts.objects.using('wp').filter(guid__icontains=f'{settings.VIDEO_BASE}{self.video.ssf_id}')
        if not video_post.exists():
            print(f"Some error for {video_post} / {self.video}")
            return
        video_post = video_post.first()
        category_id = WpTerms.objects.using('wp').get(slug=slugify(self.category.name))
        parent_category_id = WpTerms.objects.using('wp').get(
            slug=slugify(VideoCategory.objects.get(ssf_id=self.category.parent).name))

        rel1, c = WpTermRelationships.objects.using('wp').get_or_create(
            object_id=video_post.id,
            term_taxonomy_id=category_id.term_id,
            term_order=0
        )
        rel2, c1 = WpTermRelationships.objects.using('wp').get_or_create(
            object_id=video_post.id,
            term_taxonomy_id=parent_category_id.term_id,
            term_order=0
        )

        if not rel1:
            print(f"Failed to update category ({category_id.name}) for {self.video}")
            pdb.set_trace()
        if not rel2:
            print(f"Failed to update parent category ({parent_category_id.name}) for {self.video}")
            pdb.set_trace()
        print(f"{self} done")
        return


class SubscribedUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    ssf_id = models.IntegerField()
    email = models.EmailField()
    username = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    fname = models.CharField(max_length=100, null=True, blank=True)
    lname = models.CharField(max_length=100, null=True, blank=True)
    bdate = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    aboutme = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=1000, null=True, blank=True)
    town = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    zip = models.CharField(max_length=1000, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    school = models.CharField(max_length=100, null=True, blank=True)
    video_viewed = models.IntegerField(default=0)
    profile_viewed = models.IntegerField(default=0)
    watched_video = models.IntegerField(default=0)
    addtime = models.CharField(max_length=100, null=True, blank=True)
    logintime = models.CharField(max_length=100, null=True, blank=True)
    account_status = models.CharField(max_length=100, null=True, blank=True)
    subscribed = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)
    # subs_user_id=models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "SubscribedUser"
        verbose_name_plural = "2- Subscribed User"

    @staticmethod
    def populate(size=100):
        db = get_ssf_db()
        cursor = db.cursor()

        length = cursor.execute("SELECT COUNT(*) FROM signup")
        length = cursor.fetchone()[0]

        for i in range(int(length / size) + 1):
            cursor.execute(f"SELECT * FROM signup LIMIT {i * size}, {size}")
            data = cursor.fetchall()
            for subscriber in data:
                if not SubscribedUser.objects.filter(ssf_id=subscriber[0]).exists():
                    print(f"Processing: {subscriber[1]}")
                    SubscribedUser.objects.create(
                        ssf_id=subscriber[0],
                        email=subscriber[1],
                        username=subscriber[2],
                        pwd=subscriber[3],
                        fname=subscriber[4],
                        lname=subscriber[5],
                        bdate=subscriber[7],
                        gender=subscriber[8],
                        aboutme=subscriber[9],
                        website=subscriber[10],
                        town=subscriber[11],
                        city=subscriber[12],
                        address=subscriber[13],
                        zip=subscriber[14],
                        country=subscriber[15],
                        state=subscriber[16],
                        occupation=subscriber[17],
                        company=subscriber[18],
                        school=subscriber[19],
                        video_viewed=subscriber[25],
                        profile_viewed=subscriber[26],
                        watched_video=subscriber[27],
                        addtime=subscriber[28],
                        logintime=subscriber[29],
                        account_status=subscriber[30],
                        subscribed=subscriber[39]
                    )
        db.close()
        return

    @staticmethod
    def write_all_to_wp():
        subs = SubscribedUser.objects.all()
        count = subs.count()
        i = 1
        for sub in subs:
            print(f"Processing [{i}/{count}] {sub.username}")
            sub.write_to_wp()
            i += 1
        return

    def write_to_wp(self):
        old = WpUsers.objects.using('wp').filter(user_login=self.username)
        if not old.exists():
            user = WpUsers.objects.using('wp').create(
                user_login=self.username,
                user_pass=self.pwd,
                user_nicename=f"{self.fname} {self.lname}" if self.fname else self.username,
                user_email=self.email,
                user_url=self.website,
                user_registered=datetime.utcfromtimestamp(int(self.addtime)),
                user_activation_key='',
                user_status=0,
                display_name=self.username
            )

            WpUsermeta.objects.using('wp').create(
                user_id=user.id,
                meta_key='nickname',
                meta_value=self.username,
            )
            WpUsermeta.objects.using('wp').create(
                user_id=user.id,
                meta_key='wp_capabilities',
                meta_value='a:1:{s:8:"armember";b:1;}',
            )
        return


class Plan(models.Model):
    ssf_id = models.IntegerField()
    access_time_from = models.IntegerField()
    access_time_to = models.IntegerField()
    price = models.FloatField()
    package_type = models.CharField(max_length=100)
    description = models.TextField()
    sort_order = models.IntegerField()
    isdvd = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    
    type = models.CharField(max_length=100, default="Group")

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Package Plan"
        verbose_name_plural = "1-  Package Plan"

    @staticmethod
    def populate():

        db = get_ssf_db()
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM video_pacages")
        data = cursor.fetchall()
        for plan in data:

            if not Plan.objects.filter(ssf_id=plan[0]).exists():
                print(f"Processing {plan[0]} [{plan[5]}]")

                Plan.objects.create(
                    ssf_id=plan[0],
                    access_time_from=plan[1],
                    access_time_to=plan[2],
                    price=plan[3],
                    package_type=plan[4],
                    description=plan[5],
                    sort_order=plan[6],
                    isdvd=plan[7]
                )

        db.close()
        return

    def generate_csv(self):

        subs = SubscribedUser.objects.filter(sub_plan_map_s__plan_id=self.id, sub_plan_map_s__exp_date__gte=time.time())
        # id, username, email, first_name, last_name, nickname, display_name, joined, biographical_info, website
        # 1, reputeinfosystems, reputeinfosystems @ example.com, Repute, InfoSystems, reputeinfo, "Repute InfoSystems", "2016-08-01 16:08:01", " ", " "
        data = []
        i = 0
        for sub in subs:
            subscription = SubscribedUserPlanMapping.objects.filter(subscriber=sub).order_by('exp_date').last()
            data.append(
                [
                    i,
                    sub.username,
                    sub.email,
                    sub.fname,
                    sub.lname,
                    sub.username,
                    sub.username,
                    f"\"{datetime.utcfromtimestamp(subscription.exp_date).strftime('%Y-%m-%d %H:%M:%S')}\"",
                    '',
                    '',
                    sub.pwd
                ]
            )
            i += 1

        file_name = f"[{self.id}] - {self.description} - {datetime.utcnow()}.csv"

        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "username", "email", "first_name", "last_name", "nickname", "display_name", "joined", "biographical_info", "website"])
            for row in data:
                writer.writerow(row)

        print(data)

        return


class SubscribedUserPlanMapping(models.Model):
    ssf_id = models.IntegerField()
    subscriber = models.ForeignKey('SubscribedUser', related_name='sub_plan_map_s', on_delete=CASCADE)
    plan = models.ForeignKey('Plan', related_name='sub_plan_map_p', on_delete=CASCADE)
    vod_video = models.ForeignKey('Video', related_name='sub_plan_map_vod_video', on_delete=CASCADE, blank=True,
                                  null=True)
    exp_date = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"[{self.id}] {self.subscriber} <=> {self.plan}"

    class Meta:
        verbose_name = "Subscriber Plan Map"
        verbose_name_plural = "3- Subscribed User Plan Mapping"

    @staticmethod
    def populate(size=100):
        db = get_ssf_db()
        cursor = db.cursor()

        length = cursor.execute("SELECT COUNT(*) FROM uzp")
        length = cursor.fetchone()[0]

        for i in range(int(length / size) + 1):
            cursor.execute(f"SELECT * FROM uzp LIMIT {i * size}, {size}")
            data = cursor.fetchall()
            for map in data:
                subscriber = SubscribedUser.objects.filter(ssf_id=map[1])
                plan = Plan.objects.filter(ssf_id=map[3])

                if subscriber.exists() and plan.exists():
                    subscriber = subscriber.first()
                    plan = plan.first()
                    print(f"Processing: {map[0]} [{subscriber} <-> {plan}] ")
                    video = Video.objects.filter(ssf_id=map[2])

                    SubscribedUserPlanMapping.objects.create(
                        ssf_id=map[0],
                        subscriber=subscriber,
                        plan=plan,
                        vod_video=video.first() if video.exists() else None,
                        exp_date=map[4]
                    )

        db.close()

        return


class Comment(models.Model):
    ssf_id = models.IntegerField()
    video = models.ForeignKey('Video', related_name='vid_com_v', on_delete=CASCADE)
    subscriber = models.ForeignKey('SubscribedUser', related_name='vid_com_s', on_delete=CASCADE)
    comment = models.TextField()
    addtime = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.subscriber} comment on {self.video}"

    class Meta:
        verbose_name = "Video Comment"
        verbose_name_plural = "8- Video Comments"

    @staticmethod
    def populate(size=100):

        db = get_ssf_db()
        cursor = db.cursor()

        length = cursor.execute("SELECT COUNT(*) FROM comments")
        length = cursor.fetchone()[0]
        cc = 0
        for i in range(int(length / size) + 1):
            cursor.execute(f"SELECT * FROM comments LIMIT {i * size}, {size}")
            data = cursor.fetchall()

            for comment in data:
                subscriber = SubscribedUser.objects.filter(ssf_id=comment[2])
                video = Video.objects.filter(ssf_id=comment[1])

                if subscriber.exists() and video.exists():
                    # print(f"Processing: {comment[0]} [{subscriber} <-> {video}] ")
                    print('')
                    # Comment.objects.create(
                    #     ssf_id=comment[0],
                    #     subscriber=subscriber.first(),
                    #     video=video.first(),
                    #     comment=html.unescape(comment[3]),
                    #     addtime=comment[4]
                    # )
                else:
                    print(f"Missing data. Video: ({video}) {comment[1]} \ Subscriber: ({subscriber}) {comment[0]} {comment[3]}")
                    cc += 1
        pdb.set_trace()
        db.close()

        return

    @staticmethod
    def write_all_to_wp():
        # Ratings
        videos = Video.objects.filter(vid_com_v__isnull=False)
        for video in videos:
            video_post = WpPosts.objects.using('wp').get(guid=f"{settings.VIDEO_BASE}{video.ssf_id}")
            post_meta = WpPostmeta.objects.using('wp').filter(
                post_id=video_post.id,
                meta_key='_average_ratings'
            )
            if not post_meta.exists():
                post_meta = WpPostmeta.objects.using('wp').create(
                    post_id=video_post.id,
                    meta_key='_average_ratings',
                    meta_value=9
                )
            else:
                post_meta.update(meta_value=9)

        # Comments
        for comment in Comment.objects.all():
            comment.write_to_wp()
        return

    def write_to_wp(self):
        video_post = WpPosts.objects.using('wp').get(guid=f"{settings.VIDEO_BASE}{self.video.ssf_id}")
        cd = datetime.utcfromtimestamp(int(self.addtime))
        comment, c = WpComments.objects.using('wp').get_or_create(
            comment_post_id=video_post.id,
            comment_author=self.subscriber.username,
            comment_author_email=self.subscriber.email,
            comment_author_url=self.subscriber.website,
            comment_author_ip='::1',
            comment_date=cd,
            comment_date_gmt=cd,
            comment_content=self.comment,
            comment_karma=0,
            comment_approved=1,
            comment_agent='auto',
            comment_type='comment',
            comment_parent=0,
            user_id=WpUsers.objects.using('wp').get(user_login=self.subscriber.username).id
        )

        WpCommentmeta.objects.using('wp').create(
            comment_id=comment.comment_id,
            meta_key='rating',
            meta_value=9
        )

        return


class UserFavorite(models.Model):
    subscriber = models.ForeignKey('SubscribedUser', related_name='sub_fav_s', on_delete=CASCADE)
    video = models.ForeignKey('Video', related_name='sub_fav_v', on_delete=CASCADE)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.subscriber} (favs) {self.video}"

    class Meta:
        verbose_name = "User Favorite"
        verbose_name_plural = "7- User Favorite Videos"

    @staticmethod
    def populate():

        db = get_ssf_db()
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM favourite")
        data = cursor.fetchall()

        UserFavorite.objects.all().delete()

        for fav in data:
            sub = SubscribedUser.objects.filter(ssf_id=fav[0])
            video = Video.objects.filter(ssf_id=fav[1])
            if sub.exists() and video.exists():
                sub = sub.first()
                video = video.first()
                print(f"Processing: {sub} <-> {video}")
                UserFavorite.objects.create(
                    subscriber=sub,
                    video=video
                )
        db.close()

        return

    @staticmethod
    def write_all_to_wp():
        subs = SubscribedUser.objects.filter(sub_fav_s__isnull=False).distinct('id')
        for sub in subs:
            videos = Video.objects.filter(sub_fav_v__subscriber=sub)
            count = videos.count()
            vid_ids = []
            for video in videos:
                vid_ids.append(WpPosts.objects.using('wp').get(guid=f"{settings.VIDEO_BASE}{video.ssf_id}").id)

            i = 0
            s = ""
            for vid_id in vid_ids:
                s = f"{s}i:{i};i:{vid_id};"
                i += 1

            WpUsermeta.objects.using('wp').create(
                user_id=WpUsers.objects.using('wp').get(user_login=sub.username).id,
                meta_key='post_favorites',
                meta_value=f"a:{count}:{{{s}}}"
            )


def populate_all():
    Video.populate()
    VideoCategory.populate()
    VideoCategoryMapping.populate()
    Plan.populate()
    SubscribedUser.populate()
    SubscribedUserPlanMapping.populate()
    Comment.populate()
    UserFavorite.populate()
    return


def write_all_to_wp():
    Video.write_all_to_wp()
    VideoCategory.write_all_to_wp()
    VideoCategoryMapping.write_all_to_wp()
    # Plan.write_all_to_wp()
    SubscribedUser.write_all_to_wp()
    # SubscribedUserPlanMapping.write_all_to_wp()
    Comment.write_all_to_wp()
    # UserFavorite.write_all_to_wp()
    # Thumbs ({settings.THUMB_BASE}1192.jpg)
    return




class BlogPage(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.CharField(max_length=200, unique=True)
    preslug = models.CharField(max_length=200, default='1')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body_processed = models.BooleanField(default=False)
    last_processed_date = models.DateTimeField(null=True, blank=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "[{}/{}]".format(self.preslug, self.slug)

    class Meta:
        verbose_name = 'Blog Page'
        verbose_name_plural = '9- Blog Pages'

    @staticmethod
    def sync_from_wp():
        wpposts = WpPosts.objects.using('wp').filter(post_type='page', post_status='publish')
        blog, c, u = BlogPage.sync_from_wp_page(wpposts)

        return c, u

    @staticmethod
    def sync_from_wp_page(wpposts):

        pages = []
        created = 0
        updated = 0

        

