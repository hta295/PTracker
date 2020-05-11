#!/bin/sh

# Cleans up a cluster in GKE.

# Name of the cluster and kubernetes service
CLUSTER_NAME=ptracker

# Make sure we are using correct kubeconfig
gcloud container clusters get-credentials $CLUSTER_NAME

# Delete service and GKE cluster
gcloud container clusters delete $CLUSTER_NAME

