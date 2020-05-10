# Lightweight python3 parent image
FROM python:3-buster

# Setup nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.conf /etc/nginx/sites-available/default

# Copy source and install application dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/ptracker
COPY requirements.txt start-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY . /opt/app/ptracker/
WORKDIR /opt/app
RUN pip3 install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 8080
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
