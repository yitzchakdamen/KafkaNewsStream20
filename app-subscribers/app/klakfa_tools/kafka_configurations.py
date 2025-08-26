from kafka import KafkaConsumer
import json
import logging
import config
from datetime import datetime

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.getLogger('kafka').setLevel(logging.WARNING)


class KlakfaTools:

    @staticmethod
    def get_consumer(topic:str, group_id:str) -> KafkaConsumer:
        logging.info("Creating Consumer Object ..")
        return KafkaConsumer(
            topic,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            bootstrap_servers=[config.KAFKA_BOOTSTRAP_SERVERS],
            consumer_timeout_ms=10000,
            auto_offset_reset='earliest'
        )

    @staticmethod
    def get_events(consumer: KafkaConsumer) -> list:
        list_events = []
        try:
            for message in consumer:
                list_events.append({
                    "data": message.value,
                    "time": datetime.now(),
                    "timestamp": message.timestamp
                })
        finally:
            consumer.close()
            logging.info("Consumer closed.")
        print(list_events)
        return list_events