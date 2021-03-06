from connect import Connect
from pymongo import MongoClient

try:
    client = Connect.get_connection()  # connnect to database server
    db = client.data.users  # access database.collection

    mylist = [  # List of documents to add to the collection
        {"_id": 1, "name": "Edwin", "phoneNumber": "123456789", "Carrier": "Verizon"},
        {"_id": 2, "name": "Alex", "phoneNumber": "123456789", "Carrier": "Verizon"},
        {"_id": 3,
         "name": "Treshion",
         "phoneNumber": "123456789",
         "Carrier": "Verizon"},
        {"_id": 4, "name": "Devin", "phoneNumber": "123456789", "Carrier": "Verizon"},
    ]
    x = db.insert_many(mylist)  # add documents to database
except BaseException:
    print("No connection")
finally:
    client.close()
    print("Closing connection")
