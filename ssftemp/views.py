from cProfile import label
from xml.etree.ElementTree import Comment
from django.http import HttpResponse, request
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from django.db.models.expressions import F
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from ssf.models import BlogPost, VideoUpload, project_image
from ssf.models import *
from paypal_payment.models import *
import json
from django.http import JsonResponse
from django.db.models import Q
#from paypal_payment.models import Plan
# Create your views here.




# def homepage(request):  
#     dd=project_image.objects.values("image","slug")
#     p_data={}
#     for items in dd:
#         p_data.update({items["slug"]:items["image"]})


#     return render(request,'index.html' , p_data)

def get_json_from_request(request):
    output = {}
    keep_keys = ["REMOTE_HOST", "REQUEST_METHOD", "PATH_INFO", "QUERY_STRING", "REMOTE_ADDR", "HTTP_HOST",
                 "HTTP_USER_AGENT", "HTTP_REFERER", "HTTP_X_FORWARDED_FOR"]
    for key in keep_keys:
        output[key] = request.META.get(key, '')
    return output







def base_data():
    base_cbntent={ 'base_details':  project_details.objects.filter(active=True).values().first(),}
    all_videos=VideoUpload.objects.all()
    base_cbntent.update({"resent_upload":all_videos.filter(active=True,home_active=True).order_by('-modified_at')[0:3]},)
    base_cbntent.update({"cat":VideoCategory.objects.all(),})
    base_cbntent.update({"subcat":VideoSubCategory.objects.all(),})
    base_cbntent.update({
           
            'top_videos': all_videos.filter(active=True,home_active=True).order_by('-hit_count_generic__hits')[0:8],
            })
    return base_cbntent

def user_name(request):
    name=request.username
    return name

class homepage(ListView):
    model = VideoUpload
    context_object_name = 'videos'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(homepage, self).get_context_data(**kwargs)
        context['poster_data'] = VideoUpload.objects.filter(active=True,home_active=True).values('poster_url',"slug",'title','hit_count_generic','video').order_by('-hit_count_generic__hits')
        context.update(base_data())
        context["home_active"]="active"
        
        videos=VideoUpload.objects.all().filter(active=True,home_active=True).order_by('-modified_at')[0:24]
        context.update({"videos":videos})

        latest_upload=VideoUpload.objects.all().filter(active=True,home_active=True).order_by('-video_id')[0:24]
        
        context.update({"latest_upload":latest_upload})
        context.update({
            # 'popular_videos': VideoUpload.objects.values('poster_url',"slug").order_by('-hit_count_generic__hits')[:12],
            'most_populer': VideoUpload.objects.all().filter(active=True,home_active=True).order_by('-hit_count_generic__hits')[0:8],
            })
        return context

    # def get_context_data(self, **kwargs):
    #     print(kwargs)
    #     context = super(homepage, self).get_context_data(**kwargs)
    #     context.update(base_data())
    #     return context

from django.utils.decorators import method_decorator





class single_video(HitCountDetailView):
    model = VideoUpload
    template_name = 'single-video-v1.html'
    context_object_name = 'video'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True
    # login_url = '/login/'
    # redirect_field_name = 'login_user'


    # @method_decorator(login_required)
    def get_context_data(self, **kwargs):
        context = super(single_video, self).get_context_data(**kwargs)
        user=self.request.user.id
        plan=PlanSubscribedUser.objects.values().filter(user=self.request.user.id,active=True)

        # print(user,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",plan.exists())
        subscribed_status={"subscribed_status":plan.exists()}
        context.update(subscribed_status)
        if plan.exists()==False:
            subscribed_status={"subscribed_status":ViewPlan.objects.filter(video=context["video"].video_id,user=self.request.user.id,active=True).exists()}
            context.update(subscribed_status)
            #print(subscribed_status,self.request.user.id,ViewPlan.objects.filter(user=self.request.user.id).values(),"aaaaaa")
        
        # name=user_name(request)
        video_id=context["video"].video_id
        vendor_id=context["video"].vendor_id
        if vendor_id==self.request.user.id:
            subscribed_status={"subscribed_status":True}




        user_profile=UserProfile.objects.filter(user__id=user)
        if user_profile.exists():
            user_profile=user_profile.first()
            context.update({"user_profile":user_profile})

        # print(user_profile,"******************************nil((((((((")
        # print(context["video"].video_id)
        if plan.exists():

            context.update({
            'popular_videos': VideoUpload.objects.order_by('-hit_count_generic__hits')[:7],
            })
        else:
            context.update({
            # 'popular_videos': VideoUpload.objects.values('poster_url',"slug").order_by('-hit_count_generic__hits')[:12],
            'popular_videos': VideoUpload.objects.all().filter(active=True).order_by('-hit_count_generic__hits')[0:12],
            })

        context.update(base_data())
          #like dislike comment
        all=UserFavoriteVideo.objects.filter(content_type="video",content_id=video_id)
        like=all.filter(label="like").count()
        dislike=all.filter(label="dislike").count()
        fab=all.filter(fab=True).count()

        comment=UserComment.objects.filter(content_type="video",content_id=video_id).order_by("-created_at")
        cmnt=comment.count()


        video_like_data={"name":"video","like":like,"dislike":dislike,"pk":video_id,"fabrate":fab,"comment":cmnt,"comments":comment}
        context.update(video_like_data)

        if self.request.user.is_superuser == True:
            subscribed_status={"subscribed_status":True}
            context.update(subscribed_status)


        vendor_id=context["video"].vendor_id
        if vendor_id==self.request.user.id:
            subscribed_status={"subscribed_status":True}
            context.update(subscribed_status)

        # print(vendor_id==self.request.user.id,f"vendor id {vendor_id}")

        return context

    # def get_queryset(self):
    #     return PlanSubscribedUser.objects.values().filter(user=self.request.user.id)

# def homepage(request):  
#     dd=project_image.objects.values("image","slug")
#     p_data={}
#     for items in dd:
#         p_data.update({items["slug"]:items["image"]})


#     return render(request,'index.html' , p_data)

# from django.shortcuts import render

# # Create your views here.
# def  index(request):
#     return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')


def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

def login_user(request): 
    dd=project_image.objects.values("image","slug")
    urll=request.build_absolute_uri()
    pth=urll.split("login_user/?next=")
    url=pth[-1]
    url=url.replace("http://127.0.0.1:8000","")
    if "checkout" in url:
        url=url.replace("checkout/","checkout-")

    print(urll,urll,urll,urll,type(urll))
    context={}
    context.update(base_data())
    context.update({"url":url})
    if request.method == 'POST':
        username = request.POST.get('username').strip().lower()
        
        password =request.POST.get('password').strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('/login_user')
           
    
    return render(request,'login.html' , context)




def logoutUser(request):
    logout(request)
    return redirect('homepage')


def register_user(request,url="/"): 

    redirect_url=request.META
    # gdata=get_json_from_request(request)
    print(redirect_url,"*******************ok report in register****************(((((((((((((((((")
    dd=project_image.objects.values("image","slug")
    context={}
    # print("reloading 1234556")
    # urll=request.build_absolute_uri()
    # pth=urll.split("login_user/?next=")
    # url=pth[-1]
    if url !="/":
        url="/"+url
    if "checkout" in url:
        url=url.replace("checkout-","checkout/")
    print("************",url)
    context.update(base_data())

    if request.method == 'POST':
        username = request.POST.get('username').strip().lower()
        
        password =request.POST.get('password').strip()

        try:
            email =request.POST.get('email').strip()
            print(username,email,password)
            user=User.objects.filter(username=username)
            print(validateEmail( email ),"0000000000000000000000000000000000000000") # function defined abobe have to apply soon also verify email ids
            if user.exists():
                print("user name already exists ")
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect(url)
                else:
                    messages.info(request, 'Username OR password is incorrect')
                    #return redirect('/')

            else:
                user, created = User.objects.get_or_create(username=username,email=email, is_staff=0, is_active=1,)
                                                                
                user.set_password(password)
                user.save()
                user.groups.add(2)  # adding group= "register_user" id of group is 2
                print("new user created ")
                user_pro=UserProfile.objects.create(user=user,password=password,email=email)


                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    print("******&&&&&******",url)
                    return redirect(url)
                else:
                    messages.info(request, 'Username OR password is incorrect')
                    return redirect('/')


        except:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(url)
            else:
                messages.info(request, 'Username OR password is incorrect')
                return redirect('/')
            #user_id = user.pk

        #print(user.exists())


        # user_availble=User.objects.filter(is_staff=1, is_active=1,first_name=staff_First_name,last_name=school_code,email=staff_email).count()



    return render(request,'login-register.html' , context)


@login_required(login_url='register_user')
def myprofile(request):
    context={}
    user_id=request.user.id
    user = User.objects.get(id=user_id)

    user_profile=UserProfile.objects.filter(user__id=user_id)

    # comment video count
    uid=request.user.pk
    super_status=request.user.is_superuser
    all_video=VideoUpload.objects.all()
    if super_status:
        t= all_video.filter(vendor_id=0)
        total=t.count()
        context.update({"total":total})
    else:
        t=all_video.filter(vendor_id=uid)
        total= t.count()
        context.update({"total":total})
    id_tuple=t.values("video_id")

    cmnt=UserComment.objects.filter(content_type="video",content_id__in=id_tuple)   
    context.update({"comments":cmnt.count()})
     # comment video count end

    if user_profile.exists():
        user_profile=user_profile.first()
        context.update({"user_profile":user_profile})

    # user = User.objects.filter(email=email)
    # if user.exists():
    #     user = user.first()
    # else:
    #     user = User.objects.create(username=email, email=email)

    videos=all_video.filter(vendor_id=uid).order_by('-modified_at')[0:9]
    print(user,user_id,videos,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    context.update({"my_latest_videos":videos})
    context.update({
            'my_popular_videos': all_video.filter(vendor_id=uid).order_by('-hit_count_generic__hits')[0:12],
            })
    context.update(base_data())



    return render(request, 'profile-page-v1.html',context)


@login_required(login_url='register_user')
def edit_profile(request):
    context={}
    user_id=request.user.id
    usr = User.objects.filter(id=user_id)
    user=usr.first()

     # comment video count
    uid=request.user.pk
    super_status=request.user.is_superuser
    all_video=VideoUpload.objects.all()
    if super_status:
        t= all_video.filter(vendor_id=0)
        total=t.count()
        context.update({"total":total})
    else:
        t=all_video.filter(vendor_id=uid)
        total= t.count()
        context.update({"total":total})
    id_tuple=t.values("video_id")

    cmnt=UserComment.objects.filter(content_type="video",content_id__in=id_tuple)   
    context.update({"comments":cmnt.count()})
     # comment video count end

    # print(usr.values(),user)
    context.update(base_data())

    user_pro=UserProfile.objects.filter(user=user)
    # print(user_pro)
    if user_pro.exists():
        user_pro = user_pro.first()
    else:
        user_pro = UserProfile.objects.create(user=user)
    user_pro.email=user.email
    user_pro.save()

    if request.method == 'POST':
        user_pro.name=first_name=request.POST.get('name').strip()
        user_pro.email=request.POST.get('email').strip()
        user_pro.desc=request.POST.get('desc')
        if user_pro.password!=request.POST.get('password').strip():
            if request.POST.get('password').strip()==request.POST.get('re_password').strip() and request.POST.get('password').strip() is not None:
                user_pro.password=request.POST.get('password').strip()
                user.set_password(user_pro.password)  # password update to user
                user.save()

        try:   
            user_pro.image=request.FILES['image']
            usr.update(last_name=user_pro.image.url)
        except:pass
        
        user_pro.save()
        usr.update(first_name=first_name)


        user_pro=UserProfile.objects.get(user=user)
        
        # print(user_pro.image.url,"saving to lastname of user")
        # login(request, user)
        return redirect('/myprofile/')


         
    context.update({"user":user_pro})
    return render(request, 'edit_profile.html',context)


def forgot_password(request): 
    dd=project_image.objects.values("image","slug")
    context={}
    context.update(base_data())
    return render(request,'login-forgot-pass.html' , context)

def subscribe_plan(request): 
    from paypal_payment.models import Plan
    dd=project_image.objects.values("image","slug")
    context={}
    context.update(base_data())
    

    return render(request,'splan.html' , context)


#upload video
@login_required(login_url='register_user')
def submit_post(request): 
    redirect_url=request.META.get("PATH_INFO", '')
    # gdata=get_json_from_request(request)
    print(redirect_url,"***********************************(((((((((((((((((")

    dd=project_image.objects.values("image","slug")
    context={}
    context.update(base_data())
    name=request.user
    uid=request.user.pk
    super_status=request.user.is_superuser
    all_video=VideoUpload.objects.all()
    if super_status:
        t= all_video.filter(vendor_id=0)
        total=t.count()
        context.update({"total":total})
    else:
        t=all_video.filter(vendor_id=uid)
        total= t.count()
        context.update({"total":total})
    id_tuple=t.values("video_id")
    # all=UserFavoriteVideo.objects.filter(content_type="video",content_id=video_id)
    #     like=all.filter(label="like").count()
    #     dislike=all.filter(label="dislike").count()
    #     fab=all.filter(fab=True).count()
    cmnt=UserComment.objects.filter(content_type="video",content_id__in=id_tuple)
        # comment=UserComment.objects.filter(content_type="video",content_id=video_id).order_by("-created_at")
        # cmnt=comment.count()
    context.update({"comments":cmnt.count()})
    if request.method == 'POST':
        title = request.POST.get('title') 
        description =request.POST.get('description')
        metakey =request.POST.get('metakey')
        video_file =request.FILES['video_file']
        poster =request.FILES['poster']
        category=int(request.POST.get('category'))
        subcategory=int(request.POST.get('subcategory'))
        category=VideoCategory.objects.get(pk=category)
        subcategory=VideoSubCategory.objects.get(pk=subcategory)

        video=VideoUpload.objects.filter(title=title,desc=description,keywords=metakey)
        if video.exists():
            messages.info(request, 'Already exists')
        else:
            name=request.user
            uid=request.user.pk
            super_status=request.user.is_superuser

            if super_status:
                obj=VideoUpload(title=title,desc=description,keywords=metakey ,home_active=True,active=True,video=video_file,poster_image=poster,video_cat=category,vendor_id=0,sub_cat=subcategory)
                obj.save()
            else:
                obj=VideoUpload(title=title,desc=description,keywords=metakey,home_active=False ,active=False,video=video_file,poster_image=poster,video_cat=category,vendor_id=uid,sub_cat=subcategory)
                obj.save()

            print(uid,super_status,name)
            messages.success(request, "successfully saved!!")
            return redirect(f'/{obj.slug}')
            

        print(description,title)



    return render(request,'upload_video.html' , context)




#upload video
@login_required(login_url='register_user')
def upload_video(request): 
    dd=project_image.objects.values("image","slug")
    context={}
    context.update(base_data())
    if request.method == 'POST':
        title = request.POST.get('title') 
        description =request.POST.get('description')
        metakey =request.POST.get('metakey')
        video_file =request.FILES['video_file']
        poster =request.FILES['poster']
        category=int(request.POST.get('category'))
        subcategory=int(request.POST.get('subcategory'))
        category=VideoCategory.objects.get(pk=category)
        subcategory=VideoSubCategory.objects.get(pk=subcategory)

        video=VideoUpload.objects.filter(title=title,desc=description,keywords=metakey)
        if video.exists():
            messages.info(request, 'Already exists')
        else:
            name=request.user
            uid=request.user.pk
            super_status=request.user.is_superuser

            if super_status:
                obj=VideoUpload(title=title,desc=description,keywords=metakey ,home_active=True,active=True,video=video_file,poster_image=poster,video_cat=category,vendor_id=uid,sub_cat=subcategory)
                obj.save()
            else:
                obj=VideoUpload(title=title,desc=description,keywords=metakey,home_active=False ,active=False,video=video_file,poster_image=poster,video_cat=category,vendor_id=uid,sub_cat=subcategory)
                obj.save()

            print(uid,super_status,name)
            # messages.success(request, "successfully saved!!")
            print(f'/{obj.slug} (((((((((((((((((((((&&&&&&&&&&&&&&&&&&&*******************')
            return redirect(f'/{obj.slug}')
            

        print(description,title)



    return render(request,'upload_video.html' , context)

def about_us(request): 
    
    context={}
    context.update(base_data())
    context["about_active"]="active"


    return render(request,'about/about-us.html' , context)


def about_course(request): 
    
    
    context={}
    context.update(base_data())
    context["about_active"]="active"


    return render(request,'about/about_online_courses.html' , context)


def blog(request): 
    context={}
    context.update(base_data())

    context["blog_active"]="active"

    dd=project_image.objects.values("image","slug")
    p_data={}
    p_data.update(context)

    for items in dd:
        p_data.update({items["slug"]:items["image"]})

    blog_data=BlogPost.objects.values().all().order_by("-id")
    p_data.update({"blog_data":blog_data})


    return render(request,'blog.html' , p_data)



def single_blog(request,slug): 
    context={}
    context.update(base_data())

    dd=project_image.objects.values("image","slug")
    p_data={}
    p_data.update(context)

    for items in dd:
        p_data.update({items["slug"]:items["image"]})

    blog_data=BlogPost.objects.values().all()
    blog=blog_data.filter(slug=slug).first()
    p_data.update({"blog":blog})


    return render(request,'single_blog.html' , p_data)



def categories(request,slug): 
    context={}
    context.update(base_data())


    return render(request,'categories.html' , context)


def all_view(request,slug="0",sub_slug="0"): 
    

    print(slug,sub_slug)
    context={}
    context.update(base_data())
    context["category_active"]="active"
    subcat=VideoSubCategory.objects.all()
    all_video=VideoUpload.objects.all()
    count=all_video.count()
    context.update({"count":count})
    if slug=="all":
        context.update({"subcat":subcat})
        context.update({"all_video":all_video.filter(active=True).order_by('-modified_at')},)
    elif slug=="populer":
        context.update({"subcat":subcat})
        context.update({'all_video': all_video.filter(active=True).order_by('-hit_count_generic__hits')},)

    elif slug=="category":
        sbid=VideoSubCategory.objects.get(slug=sub_slug).pk
        context.update({"all_video":all_video.filter(active=True,sub_cat=sbid).order_by('-modified_at')},)

    else:
        cid=VideoCategory.objects.get(slug=slug).pk

        context.update({"subcat":subcat.filter(sub_cat=cid)})
        
        context.update({"all_video":all_video.filter(active=True,video_cat=cid).order_by('-modified_at')},)
    

        if sub_slug!="0":
            try:
                cid=VideoCategory.objects.get(slug=slug).pk
                sbid=VideoSubCategory.objects.get(slug=sub_slug).pk
                context.update({"subcat":subcat.filter(sub_cat=cid)})
                context.update({"all_video":all_video.filter(active=True,video_cat=cid,sub_cat=sbid).order_by('-modified_at')},)
            except:
                # cid=VideoCategory.objects.filter(slug=slug).first()
                sbid=VideoSubCategory.objects.get(slug=sub_slug).pk
                context.update({"all_video":all_video.filter(active=True,sub_cat=sbid).order_by('-modified_at')},)





    return render(request,'category_all_view.html' , context)


# def base(request): 
#     dd=project_image.objects.values("image","slug")
#     p_data={}
#     for items in dd:
#         p_data.update({items["slug"]:items["image"]})


#     return render(request,'base.html' , p_data)


class base(ListView):
    model =  project_details
    context_object_name = 'project_details'
    template_name = 'base.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(base, self).get_context_data(**kwargs)
        context.update({
        'popular_videos': VideoUpload.objects.order_by('-hit_count_generic__hits')[:7],
        })

        context.update({
        'base_details': project_details.objects.filter(active=True).values().first(),
        })
        return context




@login_required(login_url='register_user')
def contact_us(request): 
    context={}
    context.update(base_data())

    context["contact_active"]="active"

    user_id=request.user.pk
    user_pro=UserContactMessage.objects.filter(user_id=user_id)
    # print(user_pro)
    if user_pro.exists():
        user_pro = user_pro.first()
    else:
        user_pro = UserContactMessage.objects.create(user_id=user_id)
    
    user_pro.save()

    if request.method == 'POST':
        user_pro.user_id=user_id
        user_pro.name=request.POST.get('name').strip()
        user_pro.email=request.POST.get('email').strip()
        user_pro.subject=request.POST.get('subject').strip()
        user_pro.message=request.POST.get('message').strip()
        user_pro.save()



    return render(request,'contact_us.html' , context)



from django.core import files
from django.core.files.base import ContentFile
import mutagen
import requests
from ssf.models import VideoUpload,VideoCategory
def upload_data(request):
    data="""305//1//Are you ready for Marriage?
    354//1//Is This Love?
    306//1//Cindy Goes to a Party
    333//1//Physical Aspects of Puberty
    291//1//Human Reproduction
    288//1//How Much Affection
    289//1//Boys Beware
    292//1//Your Body During Adolescence
    105//1//Effective Sexual Functioning
    245//1//With These Weapons: The Story of Syphilis
    115//1//The History of Pornography
    117//1//Easy to Get
    215//1//Toward Emotional Maturity
    210//1//Molly Grows Up
    116//1//The Miracle of Living
    802//1//SEX MADNESS"""
    chat={"report":"running"}



    def download_by_url(url):
        r = requests.get(url, allow_redirects=True)
        filename = url.split("/")[-1]
        f=files.File(ContentFile(r.content), filename)
        return f


    def Durations(video_file):
        audio_info = mutagen.File(video_file).info
        duration = (audio_info.length)
        return int(duration) 

    inst=VideoCategory.objects.get(pk=1)
    for i in data.split("\n"):
        row=i.split("//")
        vendor_id=row[0]
        title=row[2]
        active=bool(int(row[1]))

        img_url=f"https://sexsmartfilms.com/thumb/big/{vendor_id}.jpg"
        video_url=f"https://sexsmartfilms.com/videos/{vendor_id}_1800.mp4"
    #     print(video_id,title,active)
    #     print(video_url)
        poster_image=download_by_url(img_url)
        video=download_by_url(video_url)
        duration=Durations(video)
        obj=VideoUpload(vendor_id=vendor_id,title=title,video=video,video_cat=inst,poster_image=poster_image,duration=duration,active=active)
        obj.save()
        print(vendor_id,"saved")
        
    # return render(request,'upload_data.html', {'chat':chat})


def subs(request): 
    # username = request.user.username
    # context={"user":username}
    print("********************** i m in subs ")
    body = json.loads(request.body)
    print(body)
    context={}
    print(request.method)
    _TG = "[SUBSCRIBTIONS] [NEW SUBSCRIBER]"
 
    if request.method == 'POST':
        # email = request.POST.get('email')
        email = body["email"]
        newsletter = body.get('newsletter')
        fullname = body.get('fullname')
        print(email,newsletter,fullname,"*************************email*****newsletter***")

        user = User.objects.filter(email=email)
        if user.exists():
            user = user.first()
        else:
            user = User.objects.create(username=email, email=email)

        all_sub_types = SubscriptionType.objects.all()
        all_sub_type=["Newsletter","All subscribed user"]
        if 1:
            for sub_type in all_sub_types: 
                if  sub_type.name in all_sub_type :
                    subscription = EmailSubscription.objects.filter(user=user, subscription_type=sub_type)
                    if subscription.exists():
                        subscription = subscription.first()
                        subscription.subscribed = True
                        subscription.save()
                    else:
                        EmailSubscription.objects.create(user=user, subscription_type=sub_type, subscribed=True)    
        # all_sub_types = SubscriptionType.objects.all()

        # if not email:
        #     return Response({'message': 'Email missing'}, status=status.HTTP_400_BAD_REQUEST)

        # user = User.objects.filter(email=email)
        # if user.exists():
        #     user = user.first()
        # else:
        #     user = User.objects.create(username=email, email=email)
        # # self.send_sub_email(email=email)

        # if all:
        #     for sub_type in all_sub_types:
        #         subscription = EmailSubscription.objects.filter(user=user, subscription_type=sub_type)
        #         if subscription.exists():
        #             subscription = subscription.first()
        #             subscription.subscribed = True
        #             subscription.save()
        #         else:
        #             EmailSubscription.objects.create(user=user, subscription_type=sub_type, subscribed=True)
        # logger.info(f"{_TG} {email}")

       
        # popular_posts = BlogPost.objects.all().order_by('-hit_count_generic__hits')[:5]

        # body = render_to_string('emails/newsletter_welcome.html', {
        #     'articles': popular_posts,
        #     'utm': '?utm_source=email&utm_medium=newsletter&utm_campaign=signup'
        # })
        # if not SupressEmail.objects.filter(email=email).exists():
        #     send_mail(
        #         subject="This is going to be fun",
        #         message=body,
        #         from_email=f"Shakun Sethi <shakun@tickle.life>",
        #         recipient_list=[email],
        #         fail_silently=False,
        #         html_message=body
        #     )

        # return Response({
        #     "message": user.id
        # })



        

    # return render(request,'emails/newsletter_welcome.html' , context)
    return JsonResponse({'foo':'bar'})


def add_fab(request): 

    print("********************** i m in add_fab ")
    body = json.loads(request.body)
    print(body)
    context={}
    print(request.method)
    _TG = "[SUBSCRIBTIONS] [NEW SUBSCRIBER]"
 
    if request.method == 'POST':
        # email = request.POST.get('email')
        like = body["like"]
        dislike = body.get('dislike')
        fab = body.get('fab')
        video_id = body.get('video_id')
        comment = body.get('comment')
        user_id = body.get('user_id')
        subs = body.get('subscribe')
       
        user = User.objects.get(pk=user_id)
        subscriber=subscription=EmailSubscription.objects.filter(user=user)
        if subscription.exists()==False:
            subscription_type=SubscriptionType.objects.get(name="All subscribed user")
            
            subscriber=EmailSubscription.objects.create(user=user, subscription_type=subscription_type, subscribed=True)  
        else:
            subscriber=subscriber.first()
        
        if comment!="0":
            cmt=UserComment(subscriber=subscriber,content_type="video",content_id=video_id,comment=comment)
            cmt.save()

        
        if like=="1":
            label="like"
        elif dislike=="1":
            label="dislike"

        if fab=="1":
            user_fab=UserFavoriteVideo.objects.filter(subscriber=subscriber,content_type="video",content_id=video_id,fab=True)
            print("in fab")
            if user_fab.exists()==False:

                user_fab=UserFavoriteVideo(subscriber=subscriber,content_type="video",content_id=video_id,fab=True)
                user_fab.save()


        if like=="1" or dislike=="1":
            user_fab=UserFavoriteVideo.objects.filter(subscriber=subscriber,content_type="video",content_id=video_id,label="favorite")
            if user_fab.exists():
                UserFavoriteVideo(subscriber=subscriber,content_type="video",content_id=video_id,label=label)
                
            else:
                user_fab=UserFavoriteVideo.objects.filter(subscriber=subscriber,content_type="video",content_id=video_id)
                if user_fab.exists():
                    user_fab.update(label=label)
                else:

                    user_fab=UserFavoriteVideo(subscriber=subscriber,content_type="video",content_id=video_id,label=label)
                    user_fab.save()


        

        print(like,dislike,fab,f"***********{video_id}*******{comment}***uid {user_id}****email*****newsletter***")

        # user = User.objects.filter(email=email)
        # if user.exists():
        #     user = user.first()
        # else:
        #     user = User.objects.create(username=email, email=email)

        # all_sub_types = SubscriptionType.objects.all()
        # all_sub_type=["Newsletter","All subscribed user"]
        # if 1:
        #     for sub_type in all_sub_types: 
        #         if  sub_type.name in all_sub_type :
        #             subscription = EmailSubscription.objects.filter(user=user, subscription_type=sub_type)
        #             if subscription.exists():
        #                 subscription = subscription.first()
        #                 subscription.subscribed = True
        #                 subscription.save()
        #             else:
        #                 EmailSubscription.objects.create(user=user, subscription_type=sub_type, subscribed=True)    
        



        
    video=VideoUpload.objects.filter(slug="usa-hostwithpridenonenonetrue-lets-all")
    video=video.first()
    context={"like":1111,"video":video}
    # return JsonResponse({'like':'bar'})
    return render(request,'single-video-v1.html' , context)

from django.http import JsonResponse
def video_comments(request,pk,label=None):
    user_id = request.user.pk
     
    subscription_type=SubscriptionType.objects.get(name="All subscribed user")
    subscriber=subscription=EmailSubscription.objects.filter(user_id=user_id,subscription_type=subscription_type)
    if subscription.exists()==False:
        user = User.objects.get(pk=user_id)
        
        
        subscriber=EmailSubscription.objects.create(user=user, subscription_type=subscription_type, subscribed=True)  
    else:
        subscriber=subscriber.first()
    

    video=UserFavoriteVideo.objects.filter(subscriber__user__pk=user_id,content_type="video",content_id=pk)
    if video.exists() ==False:
        video=UserFavoriteVideo.objects.create(subscriber=subscriber,content_type="video",content_id=pk)
        if label=="like":
            video.label="like"
        if label=="dislike":
            video.label="dislike"
        if label=="fab":
            video.fab=True

        if label=="subs":
            video.subscribed=True
        video.save()

    
    if video.exists():
        if label=="like":
            video.update(label="like")
        if label=="dislike":
            video.update(label="dislike")
        if label=="fab":
            video.update(fab=True)
        if label=="subs":
            video.update(subscribed=True)
        
    if label!="like" and label!="dislike" and label!="fab" and label!="ok" and  label is not None and label!="subs":
        # print("coment hai *******************************************")
        cmt=UserComment.objects.create(subscriber=subscriber,content_type="video",content_id=pk,comment=label)
        
        pass
    
        
        

    
    all=UserFavoriteVideo.objects.filter(content_type="video",content_id=pk)
    like=all.filter(label="like").count()
    dislike=all.filter(label="dislike").count()
    fab=all.filter(fab=True).count()

    comment=UserComment.objects.filter(content_type="video",content_id=pk)
    cmnt=comment.count()


    data={"name":"video","like":like,"dislike":dislike,"pk":pk,"fabrate":fab,"comment":cmnt}
    print(data,label)

    # if label=="subs":
    #     subscriber=UserFavoriteVideo.objects.filter(user_id=user_id,subscription_type=subscription_type)
    #     subscriber.update(subscribed=True)


    return JsonResponse(data,safe=False)


def search(request): 
    context={}
    context.update(base_data())
    current_url = request.path_info
    name=request.POST.get('search')
    query= request.GET.get('search')
    gdata=get_json_from_request(request)
    print("************************************************************",name,query)
    print(current_url.split)
    print(gdata)
    print("************************************************************")
    q=request.META.get("QUERY_STRING", '')
    q=q.split("&")[0]
    q=q.split("=")[1]
    # q=q.replace("search","")
    # q=q.replace("=","")
    # q=q.replace("&","")
    q=q.replace("+"," ")
    print(request.META.get("QUERY_STRING", ''))
    print(q)

    lookups= Q(title__icontains=q) #title__contains=q

    results= VideoUpload.objects.filter(lookups).distinct()
    result= BlogPost.objects.filter(lookups).distinct()
    print(results.count())
    context.update({"videos":results,"q":q,"video_count":results.count()})
    context.update({"blog_data":result,"blog_count":result.count()})


    # print(request.META)






    return render(request,'search.html' , context)