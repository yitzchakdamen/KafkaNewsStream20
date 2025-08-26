import os
from dotenv import load_dotenv

load_dotenv()

SUM_NEWS = int(os.getenv("SUM_NEWS", '10'))
KAFKA_TOPIC_INTERESTING = os.getenv("KAFKA_TOPIC_INTERESTING","")
KAFKA_TOPIC_NOT_INTERESTING = os.getenv("KAFKA_TOPIC_NOT_INTERESTING","")
APP_PUB_HOST = os.getenv("APP_PUB_HOST","localhost")
APP_PUB_PORT = int(os.getenv("APP_PUB_PORT","8080"))
KAFKA_BOOTSTRAP_SERVERS =  os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
