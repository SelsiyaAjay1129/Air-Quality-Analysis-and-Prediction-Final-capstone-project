# Air-Quality-Analysis-and-Prediction-Final-capstone-project
# Air Quality Analysis and Prediction Pipeline

## Overview

This project monitors, analyzes, and predicts air quality in Indian cities using real-time and batch data processing. The pipeline ingests, processes, and stores air quality data, making it available for analysis.

## Project Resources

### Dataset

- **India Air Quality Index Dataset**

### Tools & Technologies

- **Programming**: Python
- **Data Ingestion**: Kafka
- **Orchestration**: Airflow
- **Processing & Transformation**: Spark/Pandas
- **Storage**: Snowflake/Redshift, MongoDB/MySQL
- **Deployment**: Docker, Kubernetes
- **Monitoring**: Prometheus/Datadog
- **Cloud Providers**: AWS EC2 or local server

## Problem Statement

### Objective

- Monitor, analyze, and predict air quality in Indian cities using real-time and batch data.

### Challenges

- Handling large-scale data ingestion and processing.
- Ensuring a scalable and fault-tolerant pipeline.

## Data Model

### 1. Raw AQI Data Table

- `raw_aqi_data`: Stores raw AQI values, pollutant details, and station data.

### 2. Dimension Tables

- `dim_city`: City details (name, state, coordinates).
- `dim_date`: Date details (day, month, year).
- `dim_pollutant`: Pollutant information (name, unit).
- `dim_station`: Monitoring station details (name, city, coordinates).

### 3. Fact Table

- `fact_aqi_measurements`: Joins raw data with dimension tables for analytical queries.

## Pipeline Architecture

### 1. Ingestion

- **Kafka producers** send data to topics.
- **Kafka consumers** store raw data in MongoDB or MySQL.

### 2. Processing

- **Spark/Pandas** transform and clean the data.
- The processed data is stored in **Snowflake**.

### 3. Orchestration

- **Airflow DAGs** schedule and monitor tasks.

### 4. Deployment

- **Docker** containerizes services.
- **Kubernetes** manages containerized deployments.

## Steps for Implementation

### 1. Data Ingestion

- Develop a **Kafka producer** to ingest data into Kafka topics.
- Implement a **Kafka consumer** to store data in MongoDB/MySQL.

### 2. Data Transformation

- Develop **Spark jobs** for data cleaning and transformation.
- Load processed data into **Snowflake**.

### 3. Pipeline Orchestration

- Implement **Airflow DAGs** for scheduling tasks.

### 4. Deployment

- Containerize services using **Docker**.
- Deploy containers with **Kubernetes** for scalability.

## Deliverables

### 1. GitHub Repository

- Separate folders for each tool (Kafka, Airflow, Spark, etc.).
- **README** with detailed setup instructions.

### 2. Docker Images

- Prebuilt images for Kafka, Airflow, Spark jobs, etc.

### 3. Kubernetes Manifests

- YAML configuration files for deployment, services, and networking.

### 4. Pipeline Execution Logs

- Logs stored in **MongoDB/MySQL** and **Airflow**.

## Data Flow

### 1. Ingestion

- Store raw data in the `raw_aqi_data` table.

### 2. Transformation

- Populate dimension tables: `dim_city`, `dim_date`, `dim_pollutant`, `dim_station`.

### 3. Analytics

- Query the fact table to derive insights (e.g., **average AQI per city**, **pollutant correlation**).

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/your-repo-name/air-quality-pipeline.git
cd air-quality-pipeline
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Setup Kafka

```sh
docker-compose up -d zookeeper kafka
```

### 4. Start MongoDB or MySQL

```sh
docker-compose up -d mongodb
```

### 5. Run Kafka Producer and Consumer

```sh
python kafka_producer.py
python kafka_consumer.py
```

### 6. Run Spark Job for Data Transformation

```sh
spark-submit --master local[2] transform_data.py
```

### 7. Deploy Airflow DAGs

```sh
airflow scheduler & airflow webserver
```

### 8. Deploy to Kubernetes

```sh
kubectl apply -f kubernetes/
```

## Monitoring and Logging

- **Check Kafka logs**: `docker logs kafka`
- **Check Airflow logs**: `airflow logs`
- **View MongoDB logs**: `docker logs mongodb`
- **Monitor Prometheus**: `kubectl port-forward svc/prometheus 9090:9090`

## Future Enhancements

- Implement real-time AQI prediction using ML models.
- Deploy REST API for AQI insights.
- Integrate additional monitoring tools.

## Contributors

 SELSIYA  V

## License

MIT License

