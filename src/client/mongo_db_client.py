import pymongo
#put the connection below
host = "mongodb+srv://<username>:<password>@<xxxxxxxx>cluster.j1aik.gcp.mongodb.net/sample1?retryWrites=true&w=majority"
db = "sample_mflix"
collection_name = "login_credentials"


class MongoDBClient:
    MyClient = pymongo.MongoClient(host)
    DataBase = MyClient[db]
    Collection = DataBase[collection_name]