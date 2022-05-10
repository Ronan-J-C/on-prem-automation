# Learn Terraform - Provision a GKE Cluster

This repo is a companion repo to the [Provision a GKE Cluster learn guide](https://learn.hashicorp.com/terraform/kubernetes/provision-gke-cluster), containing Terraform configuration files to provision an GKE cluster on GCP.

This sample repo also creates a VPC and subnet for the GKE cluster. This is not
required but highly recommended to keep your GKE cluster isolated.



# Update terraform.tfvars

```
project_id = "onprem-play"
region     = "europe-west2"
cluster_name = "ronan"
```

See https://learn.hashicorp.com/tutorials/terraform/gke to set up environment and run commands

