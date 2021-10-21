import pymongo
from bson import json_util, ObjectId
from app.model.Settings import Settings
from bson.objectid import ObjectId

settings=Settings()

client = pymongo.MongoClient(settings.MONGO_DETAILS)

database = client.json_results


user=database.get_collection("user")
