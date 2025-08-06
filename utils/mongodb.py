import os
from pymongo import MongoClient


url = os.environ["MONGO_URL"]


def publish_to_mongo(article, topic, date_details):
    with MongoClient(url) as client:
        db = client["comicManagement"]
        collection = db["newsletter"]
        collection.update_one({"token": "token"}, {"$push": {"articles": {"text": article, "topic": topic, **date_details}}})

    