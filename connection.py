from pymongo import MongoClient

def connect():
    client=MongoClient('localhost',27017)
    # db=client.kinkiniroy
    return client

image_save_path="C:/Users/Deepjyoti Paul/Documents/kinkiniroy/"
image_fetch_path="http://localhost:8080/"