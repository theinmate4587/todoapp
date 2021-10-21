from bson.objectid import ObjectId
import pymongo
from datetime import datetime
from app.database.database import user

class CrudFun():
    def insert_user_details(self,data):
        
    
        #for result in results:
        document = user.find({"username": data["username"]})
        if document.count() >0:
            return "User Already Exists"
        else:
            
            result = user.insert_one(data)
            return "Regisration Done"

    def login(self,data):
        document = user.find_one({"username": data["username"]})
        if document=={} or document["password"]!=data["password"]:
            return "incorrect"
        data={}
        for field in document:
            if field!="_id":
                data[field]=document[field]
        return data
    
    def edit_user(self,username,data):
        document = user.find_one({"username": username})
        if document=={}:
            return "user not found"
        updatedData=user.update_one(
            {"username":username}, {"$set": data})
        return "updated"


        

