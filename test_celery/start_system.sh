#!/bin/sh

./restart.sh
sudo service nginx restart
uwsgi --ini test_celery_uwsgi.ini &