FROM ubuntu:20.04
RUN export DEBIAN_FRONTEND=noninteractive && apt update && apt install -y nginx python3 python3-pip uwsgi uwsgi-plugin-python3
COPY business_trips_assistant /var/www
COPY docker/uwsgi /var/www/uwsgi
COPY docker/uwsgi/uwsgi.xml /etc/uwsgi/apps-enabled/uwsgi.xml
COPY docker/nginx/default /etc/nginx/sites-enabled/default
WORKDIR /var/www
RUN pip install -r requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
