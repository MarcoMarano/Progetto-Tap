docker build ../../ --tag project:kafka

docker stop ZooKeeper
docker container rm ZooKeeper

docker run -d -e KAFKA_ACTION=start-zk --network tap --ip 10.0.100.22 -p 2181:2181 --name ZooKeeper -it project:kafka