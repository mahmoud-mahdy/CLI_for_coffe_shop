variable "credentials" {
  description = "Path to service account json file"
  # write the path to your service account json file
  default     = "C:\\Users\\ellat\\OneDrive\\Desktop\\zoom_camp_data_engineer\\My_Portfolio\\MovieLens_data_pipeline\\airflow\\keys\\cryptic-smile-413720-dcbab48aa81f.json"
}

variable "project_ID" {
  description = "The project ID"
  default     = "cryptic-smile-413720"
}

variable "region" {
  description = "The project region"
  default     = "EU"
}

variable "bucket_name" {
  description = "The name of the bucket"
  default     = "movielens-bucket"
}

variable "dataset_name" {
  description = "The name of the dataset recived from gcs"
  default     = "MovieLens"
}

variable "dbt_dev_dataset" {
  description = "The name of the dbt development dataset"
  default     = "MovieLens_dev"
}

variable "dbt_prod_dataset" {
  description = "The name of the dbt production dataset"
  default     = "MovieLens_prod"
}