import os
from dotenv import load_dotenv

load_dotenv()

sum_news = int(os.getenv("SUM_NEWS", '10'))
topic = os.getenv("KAFKA_TOPIC","")
topic_not_interesting = os.getenv("KAFKA_TOPIC_NOT_INTERESTING","")
APP_SUB_HOST = os.getenv("APP_SUB_HOST","localhost")
APP_SUB_PORT = int(os.getenv("APP_SUB_PORT","8090"))
bootstrap_servers =  os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
group = os.getenv("GROUP", "")


MONGO_HOST:str = os.getenv("MONGO_HOST", "localhost") 
MONGO_PORT:str = os.getenv("MONGO_PORT", "27017")
MONGO_DATABASE:str = os.getenv("MONGO_DATABASE", "enemy_soldiers") 
MONGO_COLLECTION:str = os.getenv("MONGO_COLLECTION", "soldier_details")