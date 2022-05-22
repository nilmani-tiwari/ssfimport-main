 source ../venv/bin/activate
 ./manage.py makemigrations
 ./manage.py migrate
 service apache2 restart
 ./manage.py runcrons "paypal_payment.cron.MyCronJob"
 

