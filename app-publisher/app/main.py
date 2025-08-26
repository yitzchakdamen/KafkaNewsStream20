from publisher import Publisher
from fastapi import FastAPI
from klakfa_tools.kafka_configurations import KlakfaTools
from kafka import KafkaProducer
import logging
import uvicorn
import config


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
publisher = Publisher()


@app.get("/api/pub-news")
async def pub_news_processing():
    producer: KafkaProducer = KlakfaTools.get_producer()
    pub_interesting_news = publisher.pub_news(producer, sum_news=config.sum_news, topic=config.topic_interesting)
    pub_not_interesting_news = publisher.pub_news(producer, sum_news=config.sum_news, topic=config.topic_not_interesting)

    if pub_interesting_news and pub_not_interesting_news: return {"status": "completed"}
    else: return {"status": "failed"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.app_pub_host, port=config.app_pub_port)
