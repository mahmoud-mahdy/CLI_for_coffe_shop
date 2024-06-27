terraform {
  required_version = ">= 1.0"
  backend "local" {} # Can change from "local" to "gcs" (for google) or "s3" (for aws), if you would like to preserve your tf-state online
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project_ID
  region      = var.region
}

# Data Lake
resource "google_storage_bucket" "data-lake-bucket" {
  name     = "${var.bucket_name}_${var.project_ID}" # Concatenating DL bucket & Project name for unique naming
  location = var.region
  versioning {
    enabled = false
  }
  force_destroy = true
  storage_class = "NEARLINE"
}

# Data Warehouse
resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.dataset_name
  project    = var.project_ID
  location   = var.region
}

resource "google_bigquery_dataset" "development_dataset" {
  dataset_id                 = var.dbt_dev_dataset
  project                    = var.project_ID
  location                   = var.region
  delete_contents_on_destroy = true
}

resource "google_bigquery_dataset" "prod_dataset" {
  dataset_id                 = var.dbt_prod_dataset
  project                    = var.project_ID
  location                   = var.region
  delete_contents_on_destroy = true
}
