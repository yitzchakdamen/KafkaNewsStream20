
from fastapi import FastAPI
from klakfa_tools.kafka_configurations import KlakfaTools
from kafka import KafkaConsumer
from data_loader import DataLoader
import os
import logging
import uvicorn
import config



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


app = FastAPI()
data_loader = DataLoader()


@app.get("/api/get_latest_pub-news")
async def pub_news_processing():
    consumer: KafkaConsumer = KlakfaTools.get_consumer(config.TOPIC, group_id=config.GROUP)
    events = KlakfaTools.get_events(consumer)
    if not events: return {"status": "no events found"}
    insert_status = data_loader.insert(events)

    if insert_status: return {"status": "completed"}
    else: return {"status": "failed"}
    
@app.get("/api/get_pub-news_from_mongo")
async def get_pub_news_from_mongo():
    events = data_loader.get_data()
    return {"data": events}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.APP_SUB_HOST, port=config.APP_SUB_PORT)  