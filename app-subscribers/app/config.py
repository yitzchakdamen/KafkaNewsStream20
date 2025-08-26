import os
from dotenv import load_dotenv

load_dotenv()

TOPIC = os.getenv("KAFKA_TOPIC","")
APP_SUB_HOST = os.getenv("APP_SUB_HOST","localhost")
APP_SUB_PORT = int(os.getenv("APP_SUB_PORT","8090"))
KAFKA_BOOTSTRAP_SERVERS =  os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
GROUP = os.getenv("GROUP", "")
MONGO_HOST:str = os.getenv("MONGO_HOST", "localhost") 
MONGO_PORT:str = os.getenv("MONGO_PORT", "27017")
MONGO_DATABASE:str = os.getenv("MONGO_DATABASE", "enemy_soldiers") 
MONGO_COLLECTION:str = TOPIC