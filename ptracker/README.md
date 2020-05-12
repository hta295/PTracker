# PTracker

PTracker is a web service where a user can submit time intervals when the user was busy. The intervals for the user are then stored in a local database for later viewing by the user.

PTracker is designed as a single-container application to be launched in a [Kubernetes](https://kubernetes.io/) cluster. Due to the use of a local, in-container database (SQLite) it is not possible to consistently coordinate multiple containers.

## Build Docker Image

```
docker build -t ptracker-server ./ptracker
```

Parent image is a lightweight linux-based python environment to which we install `nginx` (web proxy) and `gunicorn` (application server). PTracker backend is copied into image and a startup script (`start-server.sh`) as the launch entry point.

## Launch Container Locally

```
docker run -p 80:80 ptracker-server
```

This launches a PTracker container and forwards traffic on port 80 of *localhost* to the endpoint for PTracker inside of the container. This is useful for testing the container.

## Launch Kubernetes Cluster

### Provision Hardware

We are setup to use [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) for providing hardware and automated management for our Kubernetes cluster.

* To create the cluster:

```
./deployment_scripts/start_cluster.sh
```

* To teardown the cluster:

```
./deployment_scripts/cleanup_cluster.sh
```

Note that these scripts depend on the user having:
* A Google Cloud account
* Command-line access to GCP (i.e. `gcloud`) setup
* API access to Google Kubernetes engine

Creating a cluster via the command-line will configure `kubectl` to use the Kubernetes master provided by GKE as the private endpoint IP.

### Push Docker Image to GCP

The object definition for PTracker pods depends on the docker image being pushed to [gcr.io](https://cloud.google.com/container-registry), a remote container registry.

* Determine a tag for the image:

```
NAME="gcr.io/<GCP project id>/ptracker:<tag>
``` 

For example, for my GCP project and version `v0.0.2` of the image, my tag is `gcr.io/ptracker-276403/ptracker:v0.0.2`

* Tag the docker image:

```
docker tag ptracker ${NAME}
```

* Push the image to the remote image repo:

```
gcloud docker push ${NAME}
```

### Apply Kubernetes Configuration

We can use the object definitions in `./kubernetes` to create a PTracker application with:

```
kubectl apply -f kubernetes/ptracker.yaml
```

### Access

Get the external IP to reach PTracker with:

```
kubectl get services
```

Web endpoint is `<EXTERNAL IP>:8000`