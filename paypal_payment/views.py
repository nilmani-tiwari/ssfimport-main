from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib import messages
# from .models import Product, Order, LineItem
# from .forms import CartForm, CheckoutForm
# from . import cart

from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt



from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from paypal_payment.models import *
from ssf.models import *

from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required



from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'paypal_payment.my_cron_job'    # a unique code

    def do(self):
        print("**************cron************$$$$$$$$$*****************")
        pass    # do your thing here

# Create your views here.


# def show_plan(request, product_id, product_slug):
#     plan = get_object_or_404(plan, id=product_id)

#     if request.method == 'POST':
#         form = CartForm(request, request.POST)
#         if form.is_valid():
#             request.form_data = form.cleaned_data
#             cart.add_item_to_cart(request)
#             return redirect('show_cart')

#     form = CartForm(request, initial={'product_id': product.id})
#     return render(request, 'ecommerce_app/product_detail.html', {
#                                             'product': product,
#                                             'form': form,
#                                             })





from ssftemp.views import base_data


def process_payment(request,pay_view):
    print("here***********************************************")
    context={}
    context.update(base_data())

    from paypal_payment.models import Plan
    pla=Plan.objects.all().values()
    print("**********Plan",pla)
    context.update({"Plan":pla})
    pla=Plan.objects.all()
    #order_id = request.session.get('order_id')
    plan = get_object_or_404(Plan, plan_id=5)
    host = request.get_host()
    print(host,"********")

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(plan.price) ,
        'item_name': 'Order {}'.format(plan.plan_id),
        'invoice': str(plan.plan_id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    cdx={'order': plan, 'form': form}
    context.update(cdx)
    return render(request, 'paypal_payment/process_payment.html',context )


def checkout(request):
    return render(request, 'paypal_payment/checkout.html')

@login_required(login_url='login_user')
def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    
    #print("ccccccccccccccccccc",plan)
    video_id=body['video_id']
    
    user_id=request.user.pk
    pay_per_view=body['pay_per_view']
    total=body['total']

    redirect_url="/"
    if video_id==0:
        plan = Plan.objects.get(plan_id=body['productId'])
        plan_id=plan.pk
        new=PlanSubscribedUser(plan=plan_id,user=user_id,active=True,username=request.user.username,amount=plan.price)
        new.save()
        return redirect(redirect_url)
    else:
        new=ViewPlan(video=video_id,user=user_id,active=True,username=request.user.username,amount=total)
        new.save()
        ul= VideoUpload.objects.values().filter(video_id=body['video_id']).first()["slug"]
        print(ul)
        if 1:
            return redirect("/")

        return redirect("/")


    

    # user_name=request.user.username
    # email=request.user.email

    
    # Order.objects.create(
    # 	product=product
    # 	)

    #return JsonResponse('Payment completed ok report!', safe=False)

@login_required(login_url='login_user')
def checkout(request, pk,video_id=0):
    print(pk,video_id,type(video_id))
    if video_id==0:

        product = Plan.objects.get(plan_id=pk)
        context = {'product':product}
        context.update(base_data())
        plan_title_details={"plan_title":"1. Subscription Plans","video_id":video_id,"pay_per_view":False,"slug":"A-Recipe-for-Disaster"}
        context.update(plan_title_details)
        #print(pk,video_id,type(video_id))
        return render(request, 'paypal_payment/checkout.html', context)
    else:
        product={"price":0.99}
        plan_title_details={"plan_title":"2. Pay Per View ","video_id":video_id,"pay_per_view":False}
        context = {'product':product}
        context.update(base_data())
        context.update(plan_title_details)
        video_detail=VideoUpload.objects.values('poster_url',"slug","video_id").filter(video_id=video_id).first()
        context.update(video_detail)
        return render(request, 'paypal_payment/checkout.html', context)


# trying another way

def process_payment(request,pay_view="0-0"):

    

    context={}
    
    context.update(base_data())
    if pay_view !="0-0" and pay_view is not None :
        pay_view=pay_view.split("-")
        video_id=int(pay_view[1])
        video_detail=VideoUpload.objects.values('poster_url',"slug","video_id","title").filter(video_id=int(pay_view[1])).first()["title"]
        context.update({"video_title":video_detail})
        context.update({"view_price":0.99,"view_id":int(pay_view[1]),"pay_per_view":True})
    from paypal_payment.models import Plan
    pla=Plan.objects.all().values()
    # print("**********Plan",pla)
    context.update({"plan":pla})
    if request.method == 'POST' :
        selector = request.POST.get('selector')
        print(selector,"sssssssssssssssssssssssssssssssssssssssssssss",str(selector) in pay_view)
        
    

        if selector is not None and pay_view=="0-0":
            pk=int(selector)
            return redirect(f'/checkout/{pk}')

        elif selector is not None and str(selector) not in pay_view:
            pk=int(selector)
            return redirect(f'/checkout/{pk}')
        else:
            return redirect(f'/checkout/99/{video_id}')
            
        
        


    return render(request, 'paypal_payment/process_payment.html',context )

@csrf_exempt
def payment_done(request):
    return render(request, 'paypal_payment/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'paypal_payment/payment_cancelled.html')






#**********************************************error functions**************************************


from django.shortcuts import render

def error_404(request,  *args, **kwargs):
    context={}
    context.update(base_data())

    return render(request,'500.html',context)

def error_500(request,  *args, **kwargs):
    context={}
    context.update(base_data())
    data={}
    return render(request,'500.html', context)
        
def error_403(request,  *args, **kwargs):
    context={}
    context.update(base_data())

    return render(request,'500.html',context)

def error_400(request,   *args, **kwargs):
    context={}
    context.update(base_data())
    data={}
    return render(request,'500.html', context)  





