#!/usr/bin/env bash
# Build image
docker build ./src/ --tag project:spark

# Stop previuos container
docker stop sparkProcessing
# Remove previuos container 
docker container rm sparkProcessing

echo "Waiting for Kafka to start Spark..."

while ! nc -z 10.0.100.23 9092; do
  printf '.'
  sleep 1
done

echo "Kafka launched"

gnome-terminal --title="Spark Processing" -x sh -c 'docker run -e SPARK_ACTION=spark-submit-python --network tap --name sparkProcessing -it project:spark data_cleaner.py org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.5'

# Stop previuos container
docker stop sparkMLlib
# Remove previuos container 
docker container rm sparkMLlib

gnome-terminal --title="Spark MLlib" -x sh -c 'docker run -e SPARK_ACTION=spark-submit-python --network tap --name sparkMLlib -it project:spark data_analysis.py org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.5'

# Stop previuos container
#docker stop sparkMergeData
# Remove previuos container 
#docker container rm sparkMergeData

#gnome-terminal --title="Spark Merge Data" -x sh -c 'docker run -e SPARK_ACTION=spark-submit-python --network tap --name sparkMergeData -it project:spark merge_data.py org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.5'