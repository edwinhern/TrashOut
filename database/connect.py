from pymongo import MongoClient
import dns


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient(
            "test")
