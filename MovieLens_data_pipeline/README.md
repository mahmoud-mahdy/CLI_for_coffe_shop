# MovieLens data pipeline Project

## Table of Contents
- [MovieLens data pipeline Project](#movielens-data-pipeline-project)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Problem description](#problem-description)
  - [dataset](#dataset)
      - [Dataset source:](#dataset-source)
      - [Overview:](#overview-1)
  - [Technologies](#technologies)
  - [Project architecture](#project-architecture)
  - [Dashboard](#dashboard)
      - [More details about the project are available in each folder readme file](#more-details-about-the-project-are-available-in-each-folder-readme-file)
  - [Replication :](#replication-)
      - [Prerequisites (things you will need to have before):](#prerequisites-things-you-will-need-to-have-before)
      - [instructions:](#instructions)
        - [Cloning and setting up the project:](#cloning-and-setting-up-the-project)
        - [Terraform:](#terraform)
        - [Environment variables:](#environment-variables)
        - [Airflow:](#airflow)
        - [DBT (data build tool):](#dbt-data-build-tool)
        - [Looker Studio](#looker-studio)

## Overview
A batched end-to-end data pipeline for movies data. the pipeline gets the data from [MovieLens](https://movielens.org/) website and sends it to Google Cloud storage then to bigquery then to DBT (data build tool) where the data transformation then to the dashboard in Looker Studio to be visualised.

This project is based on [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) course held by [DataTalks.Club](https://datatalks.club/) to implement everything taught in the course and build an end-to-end data pipeline.

## Problem description
Using the data to answer some key questions such as what are the most rated movies on the website? How accurate are tags given by users to the movies? Who are the most valuable users of the websites? 

Project goals:
* building ELT end-to-end batch data pipeline that processes the data on a monthly basis.
* build a Dashboard that will help in visualizing the data and extract useful information that helps the website.

## dataset
#### Dataset source:
[MovieLens Latest Datasets](https://grouplens.org/datasets/movielens/) under MovieLens Latest Datasets full version

#### Overview:
The dataset from [MovieLens](https://movielens.org/) website is a 5-star rating system for movies. 

* It comprises ≈ 33M ratings and ≈ 2M tag applications for ≈ 86K movies, created by ≈ 331K users from January 9, 1995, to July 20, 2023.

* Users were randomly selected and had rated at least one movie. No demographic information is included; each user is identified only by an ID.

* The dataset composes of six files which are genome-scores.csv, genome-tags.csv, links.csv, movies.csv, ratings.csv, and tags.csv.

* (tags.csv table) was not used in the dashboard as it was not very useful. The dataset gets updated over time however the download link doesn't change

The following diagram helps in visualizing the dataset and shows the database relationship:


![database relationship](<Images/database relationship.png>)

More information about the dataset is available here: [dataset_description](dataset.txt)
## Technologies
The project uses the following technologies:

* Workflow orchestration:  <img src="Images/airflow.png" alt="airflow" width="60">
* Cloud:  <img src="Images/Google_Cloud_logo.svg.png" alt="google cloud" width="135">
  * Data Lake (DL): GCS
  * Data Warehouse (DWH): BigQuery
* Infrastructure as code (IaC):  <img src="Images/Terraform_Logo.svg.png" alt="terraform" width="100">
* Transforming data:  <img src="Images/dbt-logo.png" alt="dbt" width="65">
* Data Visualization: <img src="Images/Looker.svg.png" alt="Looker studio" width="100">

## Project architecture
The end-to-end batch pipeline as shown in the diagram below:
* Download the data from URL and transform it from csv to parquet.
* Load the data into GCS (data lake)
* Load the data from GCS into BigQuery (DWH)
* Transform the data using DBT(Data Build Tool) in the BigQuery
* Load the data from BigQuery to Looker Studio

![project_architect](Images/project_architect.png)

## Dashboard

The Dashboard can be accessed in the using the following link: [Dashboard](https://lookerstudio.google.com/reporting/a937b3d1-6f12-4857-827d-347ab817960d)

Note: Most accurate tags table take more time please be patient. It has to go through more data than the reset.

![dashboard](Images/dashboard.png)

Controls have been added making the dashboard interactive. Filters can be added to get movies based on the specific year or specific genre.

Most valuable users to the websites as they made the most contributions, most accurate tags given by user compared to the tags given by the website using machine learning model

#### More details about the project are available in each folder readme file

## Replication :

#### Prerequisites (things you will need to have before):
* docker
* terraform
* Google Cloud account (you can use the trial version)
* DBT (Data Build Tool) account (you can use the free version)

#### instructions:
The instruction  below can be followed to replicate the project:

##### Cloning and setting up the project:

Because you cloning a subdirectory of the repo the usual git clone command will be a bit different so you will need to do the following:

```
mkdir ML_repo
cd ML_repo
git init
git remote add -f origin https://github.com/mahmoud-mahdy/My_Portfolio.git
git config core.sparseCheckout true
echo "MovieLens_data_pipeline" >> .git/info/sparse-checkout
git pull origin main
```
Please make a service account and give bigquery and GCS permissions (you can use bigquery admin and gcs admin as a quick setup for the project although not recommended for bigger projects).
Also, you can use the same service account for both airflow and terraform just as a quick setup.

please download the key of the service account and save it in
(airflow\keys)

##### Terraform:
Go to [variables.tf](terraform/variables.tf) and edit the values according to your project. (credentials, project_id) and maybe region if not in the EU.

Start a new terminal in the main directory

building the resources on Google Cloud
```
cd terraform
terraform init
terraform apply
 ```
Type yes if promoted to confirm the above command.

Go to your Google Cloud account and get the bucket name created it should be <bucket_name>_<project_id>

if you would like to destroy all resources at the end of the project please run in terminal ```terraform destroy```

##### Environment variables:
please open up the [.env_example](.env_example) and fill it with your values PROJECT_ID, BUCKET_NAME

start new terminal in main directory
```
mv example.env airflow/.env
```

##### Airflow:
Start a new terminal in the cloned repo directory

Please make sure the docker is already running.
```
cd airflow
docker-compose up -d --build
```
Please be patient as it can take up to 10 minutes depending on your pc and internet speed.

when finished open http://localhost:8080/ in your browser username ```airflow``` password ```airflow```

open ```admin``` then ```connection``` then make new connection called ```gcloud```
and write the path to the service account key downloaded earlier.
```/opt/airflow/keys/<service_account.json```

replace ```<service_account.json>``` with your key name

Go back and run first dag ```download_dataset_and_upload_to_gsc_dag.py``` then the second```gsc_to_bq_dag.py``` 

First dag should send the data to gcs and the second should send it to the big query.

##### DBT (data build tool):
Create an account (if you don't already have one) by clicking [here](https://www.getdbt.com/signup/) you can just follow the instructions and create an account, and here is documentation about how to do so if you need it click [here](https://docs.getdbt.com/docs/cloud/manage-access/set-up-bigquery-oauth) 

Remember to write the dataset ```MovieLens_dev``` when setting up as the Dataset of the Development credentials.

if you forgot to do so you can go to settings > Credentials > the name of your project > Development credentials > ```MovieLens_dev```

you can fork this repo and choose the subdirectory DBT in this repo.

after setting the development environment run ```dbt build --vars '{'is_test_run': 'false'}'```
this will transform all the data and store it in ```MovieLens_dev``` in bigquery.

Go to environments and make a new environment call it production with ```MovieLens_prod``` dataset and this will be the production environment now you can make a new deploy job and choose the production environment you can make it weekly and write the following commands


```
dbt build --vars '{'is_test_run': 'false'}'
dbt test
```
check ```generate docs``` and ```source freshness``` both are already set to work in the code.

Note: when running any query it will be limited to only 100 results this has been set to make the development faster therefore in production we remove the limit using ```'{'is_test_run': 'false'}'```  

```dbt test``` will run all the tests sets and source freshness will run automatically in the beginning.

Now you have both a development and production environment.

To set CI (continuous integration) go to jobs > create new job > continuous integration job

set the environment to production
and trigger by pull request should be checked

Commands
```
dbt build --select state:modified+ --vars '{'is_test_run': 'false'}'
dbt test
```

Now the CI job will work automatically when you do a pull request it will run all changes then do the tests set to make sure nothing broke in the code which helps a lot in speeding development and building trust and is considered a best practice. 

You can check the documentation and the source's freshness as well in the interface.

##### Looker Studio

The dashboard is just straightforward to make and doesn't need specific instructions to follow you can watch any YouTube video on how to make it (that will be easier to follow).
