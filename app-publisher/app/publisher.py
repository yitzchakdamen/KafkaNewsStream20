from sklearn.datasets import fetch_20newsgroups
import sklearn_categories
from klakfa_tools.kafka_configurations import KlakfaTools
from kafka import KafkaProducer
import logging
import config


class Publisher:
    
    def __init__(self) -> None:
        self.offset=0
        self.newsgroups_interesting=fetch_20newsgroups(subset='all',categories=sklearn_categories.interesting_categories, data_home='./scikit_learn_data' )
        self.newsgroups_not_interesting=fetch_20newsgroups(subset='all',categories=sklearn_categories.not_interesting_categories, data_home='./scikit_learn_data' )

    def pub_news(self, producer:KafkaProducer, sum_news:int, topic:str) -> bool:
        
        news = self.newsgroups_interesting.data if topic == config.KAFKA_TOPIC_INTERESTING else self.newsgroups_not_interesting.data
        
        if self.offset + sum_news > len(news):
            logging.warning("Not enough news articles to publish.")
            return False

        for i in range(self.offset, self.offset + sum_news):
            KlakfaTools.publish_send_message(producer=producer, topic=topic, key=None, message=news[i])
            
        self.offset += sum_news
        return True
    