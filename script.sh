 source ../venv/bin/activate
 ./manage.py makemigrations
 ./manage.py migrate
 service apache2 restart
