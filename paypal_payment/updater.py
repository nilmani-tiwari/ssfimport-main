
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
# from forecastUpdater import forecastApi
from .cron import my_cron_job

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_cron_job, 'interval', minutes=1440)
    print("in updator running my_cron_job***********")
    scheduler.start()