# Garbage Classification Using Hadoop & Hive 🗂️

An end-to-end Big Data pipeline that classifies 12,260 garbage 
images across 10 categories using Hadoop MapReduce and Apache Hive.

## What it does
Processes large-scale image metadata through a distributed pipeline,
runs analytical HiveQL queries, and surfaces insights via an 
interactive Power BI dashboard.

## Tech Stack
`Python` `Apache Hadoop` `Apache Hive` `Docker Compose` `Power BI`

## Pipeline Overview
1. Python script extracts metadata from 12,260 image records → CSV
2. CSV loaded into Hadoop HDFS for distributed storage
3. Apache Hive runs 4 HiveQL queries as MapReduce jobs across 1.7MB
4. Results: category distribution, frequency counts, anomaly insights
5. Power BI dashboard with 6 visuals and filters across 10 classes

## Key Stats
- 12,260 records across 10 garbage categories
- Full MapReduce execution in under 5 minutes
- 5 containerized services via Docker Compose
- 6-visual interactive Power BI dashboard

## Run Locally
docker-compose up
# Hadoop UI: http://localhost:9870
# Hive: connect via beeline
