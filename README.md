# PTracker

## Launch in Container with Docker

To launch a PTracker server as a container in Docker on localhost:

### Build image:

```
docker build -t ptracker-server .
```

Parent image is a lightweight linux-based python environment to which we install `nginx` (web proxy) and `gunicorn` (application server). PTracker backend is copied into image and a startup script (`start-server.sh`) as the launch entry point.

Note that currently we copy the local DB file into the image. As a consequence, when run as a container, no DB writes persist and the DB cannot be shared by multiple web servers. TODO: extract DB into its own container.

* Launch container:

```
docker run -p 80:80 ptracker-server
```

This launches a PTracker web server
