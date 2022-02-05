import pymysql
from django.conf import settings


def get_ssf_db():
    ssf_db = settings.SSF_DB

    return pymysql.connect(
        host=ssf_db.get('host'),
        user=ssf_db.get('username'),
        password=ssf_db.get('password'),
        database=ssf_db.get('db_name')
    )
