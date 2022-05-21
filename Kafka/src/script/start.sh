docker build ../../ --tag project:kafka

docker container rm kafkaServer

docker run -d -e KAFKA_ACTION=start-kafka --network tap --ip 10.0.100.23  -p 9092:9092 --name kafkaServer -it project:kafka