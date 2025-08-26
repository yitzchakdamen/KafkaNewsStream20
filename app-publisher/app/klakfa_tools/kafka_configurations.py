from kafka import KafkaProducer
import json
import logging
import config

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.getLogger('kafka').setLevel(logging.WARNING)


class KlakfaTools:

    @staticmethod
    def get_producer() -> KafkaProducer:
        logging.info("Creating producer object ..")
        return KafkaProducer(bootstrap_servers=[config.bootstrap_servers],value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    @staticmethod
    def publish_send_message(producer:KafkaProducer,  topic, key, message):
        logging.info(f"Publish json messages with key --->> {str(key)}, to topic -->> {str(topic)}")
        producer.send(topic, key=key, value=message)
        producer.flush()




