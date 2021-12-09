from connect import Connect
from pymongo import MongoClient
import dns

try:
    client = Connect.get_connection() 
    db = client["test"]
    coll = db["test"]
    coll.insert_one({"name": "Edwin"})
except:
    print("No connection")
finally:
    client.close()
    print("Closing connection")

 