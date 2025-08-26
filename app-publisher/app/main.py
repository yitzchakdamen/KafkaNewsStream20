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
    pub_interesting_news = publisher.pub_news(producer, sum_news=config.SUM_NEWS, topic=config.KAFKA_TOPIC_INTERESTING)
    pub_not_interesting_news = publisher.pub_news(producer, sum_news=config.SUM_NEWS, topic=config.KAFKA_TOPIC_NOT_INTERESTING)

    if pub_interesting_news and pub_not_interesting_news: return {"description": "published news to kafka", "status": "completed", "published count for each topic": config.SUM_NEWS}
    else: return {"status": "failed"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.APP_PUB_HOST, port=config.APP_PUB_PORT)