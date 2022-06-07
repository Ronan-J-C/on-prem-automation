variable "project_id" {
  description = "project id"
}

variable "region" {
  description = "region"
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# VPC
resource "google_compute_network" "vpc" {
  name                    = "${var.cluster_name}-vpc"
  auto_create_subnetworks = "false"
}

# Subnet
resource "google_compute_subnetwork" "subnet" {
  name          = "${var.cluster_name}-subnet"
  region        = var.region
  network       = google_compute_network.vpc.name
  ip_cidr_range = "10.10.0.0/24"
}


resource "google_compute_address" "external_ip" {
  name = "${var.cluster_name}-gke"
}

resource "google_compute_firewall" "firewall_rules" {

  name    = "k8s-firewall-rules"

  network = google_compute_network.vpc.name

  allow {

    protocol = "all"

  }


  target_tags    = ["gke-node", "${var.cluster_name}-gke"]

  source_ranges = [
                      "192.195.83.11/32",
                      "125.19.67.142/32",
                      "207.242.51.98/32",
                      "35.197.25.142/32",
                      "35.212.161.151/32",
                      "34.105.89.11/32",
                      "10.12.0.0/14",
                      "35.233.182.198/32", 
                      "35.203.167.5/32",
                      "10.76.0.0/20",
                      "35.199.180.244/32", 
                      "35.233.145.199/32",
                      "65.115.92.26/32",
                      "34.105.84.218/32",
                      "34.93.204.95/32",
    ]
  //source_ranges = ["${var.restricted_src_address}"]  // for real

}