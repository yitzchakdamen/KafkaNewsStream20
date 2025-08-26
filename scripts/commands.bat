

cd C:\Users\isaac\source\repos\BlockingVsNoneBlocking

@REM --- kafka ---
docker run -d --name kafka-broker -p 9092:9092 apache/kafka:latest

@REM --- mongodb ---
docker run -d --name mongodb-NewsStream20 -p 27017:27017 mongodb/mongodb-community-server

@REM --- subscribers ---

cd C:\Users\isaac\source\repos\KafkaNewsStream20\app-subscribers
docker build -t app-subscribers .

docker run -d --name app-subscribers-1 ^
    -e APP_SUB_HOST=0.0.0.0 ^
    -e APP_SUB_PORT=8001 ^
    -e KAFKA_BOOTSTRAP_SERVERS=localhost:9092 ^
    -e KAFKA_TOPIC=interesting_news ^
    -e MONGO_HOST=localhost ^
    -e MONGO_PORT=27017 ^
    -e MONGO_DATABASE=NewsStream20Public ^
    -e MONGO_COLLECTION=interesting-news ^
    -e GROUP=group_interesting_news_1 ^
    -p 8001:8001 app-subscribers

docker run -d --name app-subscribers-2 ^
    -e APP_SUB_HOST=0.0.0.0 ^
    -e APP_SUB_PORT=8002 ^
    -e KAFKA_BOOTSTRAP_SERVERS=localhost:9092 ^
    -e KAFKA_TOPIC=not_interesting_news ^
    -e MONGO_HOST=localhost ^
    -e MONGO_PORT=27017 ^
    -e MONGO_DATABASE=NewsStream20Public ^
    -e MONGO_COLLECTION=not_interesting_news ^
    -e GROUP=group_not_interesting_news_1 ^
    -p 8002:8002 app-subscribers


@REM --- publisher ---

cd C:\Users\isaac\source\repos\KafkaNewsStream20\app-publisher
docker build -t app-publisher .

docker run -d --name app-publisher ^
    -e KAFKA_TOPIC_INTERESTING=interesting_news ^
    -e KAFKA_TOPIC_NOT_INTERESTING=not_interesting_news ^
    -e APP_PUB_HOST=0.0.0.0 ^
    -e APP_PUB_PORT=8080 ^
    -e KAFKA_BOOTSTRAP_SERVERS=localhost:9092 ^
    -e SUM_NEWS=10 ^
    -p 8080:8080 app-publisher