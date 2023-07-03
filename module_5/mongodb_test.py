from pymongo import MongoClient
url = "mongodb+srv://<username>:<password>@cluster0.arleilq.mongodb.net/"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names)
