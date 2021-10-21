import os
class Settings():
    
    secret_key="todoapp"
    if 'MONGO_USERNAME'in os.environ:
        MONGO_DETAILS = "mongodb://%s:%s@%s" % (os.environ["MONGO_USERNAME"], os.environ["MONGO_PASSWORD"], os.environ["MONGO_HOST"])

    else:
        MONGO_DETAILS="mongodb://127.0.0.1:27017"