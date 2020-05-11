#!/bin/sh

# Creates new GKE cluster

set -e

# Name of cluster
CLUSTER_NAME=ptracker
# Number of nodes to launch in cluster
NUM_NODES=1
# Machine type for the GKE cluster
MACHINE_TYPE=e2-medium

# Startup and run cluster
gcloud container clusters create $CLUSTER_NAME --num-nodes=$NUM_NODES --machine-type=$MACHINE_TYPE

