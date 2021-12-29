#!/bin/bash
python3 manage.py migrate;
python3 manage.py collectstatic --noinput;
printenv | grep -v "no_proxy" >> /etc/environment;
/etc/init.d/uwsgi start;
nginx -g "daemon off;";