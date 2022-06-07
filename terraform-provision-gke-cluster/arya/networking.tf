variable "project_id" {
  description = "project id"
}

variable "region" {
  description = "region"
}
variable "cluster_name" {
  description = "project id"
}
provider "google" {
  project = var.project_id
  region  = var.region
}



resource "google_compute_address" "external_ip" {
  name = "${var.cluster_name}-gke"
}