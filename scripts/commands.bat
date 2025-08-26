docker network create KafkaNewsStream20

cd C:\Users\isaac\source\repos\BlockingVsNoneBlocking

@REM --- kafka ---

docker run -d --name kafka-broker ^
    --network KafkaNewsStream20 ^
    -p 9092:9092 -p 9093:9093 ^
    -e KAFKA_NODE_ID=1 ^
    -e KAFKA_PROCESS_ROLES=broker,controller ^
    -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 ^
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka-broker:9092 ^
    -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER ^
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@kafka-broker:9093 ^
    -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 ^
    -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 ^
    -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 ^
    -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 ^
    apache/kafka:latest


@REM --- mongodb ---
docker run -d --name mongodb-NewsStream20 --network KafkaNewsStream20  -p 27017:27017 mongodb/mongodb-community-server

@REM --- subscribers ---

cd C:\Users\isaac\source\repos\KafkaNewsStream20\app-subscribers
docker build -t app-subscribers .

docker run -d --name app-subscribers-1 ^
    -e APP_SUB_HOST=0.0.0.0 ^
    -e APP_SUB_PORT=8001 ^
    -e KAFKA_BOOTSTRAP_SERVERS=kafka-broker:9092 ^
    -e KAFKA_TOPIC=interesting_news ^
    -e MONGO_HOST=mongodb-NewsStream20 ^
    -e MONGO_PORT=27017 ^
    -e MONGO_DATABASE=NewsStream20Public ^
    -e GROUP=group_interesting_news_1 ^
    --network KafkaNewsStream20 ^
    -p 8001:8001 app-subscribers

docker run -d --name app-subscribers-2 ^
    -e APP_SUB_HOST=0.0.0.0 ^
    -e APP_SUB_PORT=8002 ^
    -e KAFKA_BOOTSTRAP_SERVERS=kafka-broker:9092 ^
    -e KAFKA_TOPIC=not_interesting_news ^
    -e MONGO_HOST=mongodb-NewsStream20 ^
    -e MONGO_PORT=27017 ^
    -e MONGO_DATABASE=NewsStream20Public ^
    -e GROUP=group_not_interesting_news_1 ^
    --network KafkaNewsStream20 ^
    -p 8002:8002 app-subscribers


@REM --- publisher ---

cd C:\Users\isaac\source\repos\KafkaNewsStream20\app-publisher
docker build -t app-publisher .

docker run -d --name app-publisher ^
    -e KAFKA_TOPIC_INTERESTING=interesting_news ^
    -e KAFKA_TOPIC_NOT_INTERESTING=not_interesting_news ^
    -e APP_PUB_HOST=0.0.0.0 ^
    -e APP_PUB_PORT=8080 ^
    -e KAFKA_BOOTSTRAP_SERVERS=kafka-broker:9092 ^
    -e SUM_NEWS=10 ^
    --network KafkaNewsStream20 ^
    -p 8080:8080 app-publisher