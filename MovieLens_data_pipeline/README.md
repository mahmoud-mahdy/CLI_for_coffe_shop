# MovieLens data pipeline Project
## Overview
This project is based on [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) course held by [DataTalks.Club](https://datatalks.club/) with the goal of implementing everything tought in the course and build an end-to-end data pipeline.

## Problem description

## dataset
#### Dataset source:
[MovieLens Latest Datasets](https://grouplens.org/datasets/movielens/) under MovieLens Latest Datasets full version
#### Overview:
This dataset, from [MovieLens](https://movielens.org/) website , includes 5-star ratings and free-text tagging activity. 

It comprises ≈ 33M ratings and ≈ 2M tag applications for ≈ 86K movies, created by ≈ 331K users from January 9, 1995, to July 20, 2023.

Users were randomly selected and had rated at least one movie. No demographic information is included; each user is identified only by an ID.

The dataset composes of six files which are genome-scores.csv, genome-tags.csv, links.csv, movies.csv, ratings.csv, and tags.csv. the dataset gets updated overtime however the download link doesnt change

The following diagram help in visualizing the dataset and show the database relationship:

![database relationship](<Images/database relationship.png>)

More information about the dataset available here: [dataset_description](dataset.txt)
## Technologies
We are going to use the following technologies for this project:

* Workflow orchestration: Airflow
* Cloud: GCP
  * Data Lake (DL): GCS
  * Data Warehouse (DWH): BigQuery
* Infrastructure as code (IaC): Terraform
* Transforming data: DBT (Data Build Tool)
* Data Visualization: Google Looker Studio

## Project architecture

![project_architect](Images/project_architect.png)

## dashboard link

https://lookerstudio.google.com/reporting/a937b3d1-6f12-4857-827d-347ab817960d

