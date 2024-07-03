![terraform](../Images/Terraform_Logo.svg.png)

Terraform is an open source infrastructure-as-code tool. It enables you to build, change, and manage infrastructure in your cloud environment.

Terraform has been used to automate building the resources and destroy them at the end of the project.

The resources built by terraform are:
* Data lake:
  * GCS bucket
  * Object in the bucket (folder called pq/)
* Data warehouse:
  * Dataset (To store data coming from Data lake)
  * Dataset (for development)
  * dataset (for production)