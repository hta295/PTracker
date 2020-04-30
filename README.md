# PTracker

## Launch in Container with Docker

To launch a PTracker server as a container in Docker on localhost,

* Build image:

```
docker build -t ptracker-server .
```

* Launch container:

```
docker run -p 0.0.0.0:8080:8000 ptracker-server
```
