import os
from dotenv import load_dotenv

load_dotenv()

sum_news = int(os.getenv("SUM_NEWS", '10'))
topic_interesting = os.getenv("KAFKA_TOPIC_INTERESTING","")
topic_not_interesting = os.getenv("KAFKA_TOPIC_NOT_INTERESTING","")
app_pub_host = os.getenv("APP_PUB_HOST","localhost")
app_pub_port = int(os.getenv("APP_PUB_PORT","8080"))
bootstrap_servers =  os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
