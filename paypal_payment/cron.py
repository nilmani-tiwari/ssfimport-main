from django_cron import CronJobBase, Schedule
from paypal_payment.models import *
from datetime import datetime
from datetime import timedelta
from datetime import date

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'paypal_payment.my_cron_job'    # a unique code

    def do(self):
        obj=s3control(active=True)
        obj.save()
        print("**************cron************$$$$$$$$$*****************")
        pass    # do your thing here


from django.core.management.base import BaseCommand, CommandError
import os
from crontab import CronTab

class Command(BaseCommand):
    help = 'Cron testing'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #init cron
        cron = CronTab(user='your_username')

        #add new cron job
        job = cron.new(command='python <path_to>/example.py >>/tmp/out.txt 2>&1')

        #job settings
        job.minute.every(1)

        cron.write()

import datetime


def my_cron_job():
    from paypal_payment.models import ViewPlan
    # your functionality goes here
    today_now = datetime.datetime.now()
    obj=s3control(active=False)
    obj.save()
    data=ViewPlan.objects.filter(active=True).update(active=False)
    Begindatestring = date.today()
    # sdata=PlanSubscribedUser.objects.filter(expiry_date=Begindatestring)
    sdata=PlanSubscribedUser.objects.filter(expiry_date__lt=today_now)
    sdata.update(active=False)
    # print(sdata.expiry_date==Begindatestring,sdata.expiry_date,Begindatestring)
    print(Begindatestring,"*****",today_now)

    
    print("**************cron************$$$$$$22222$$$*****************")