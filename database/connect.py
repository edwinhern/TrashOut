from pymongo import MongoClient
import dns 

class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient("mongodb+srv://ehh0025:Edstriker77@cluster1.9ri6z.mongodb.net/test?retryWrites=true&w=majority")
    
        