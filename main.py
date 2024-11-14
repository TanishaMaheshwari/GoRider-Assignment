import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://mongo:27017/')
    db = client['user']
    collection = db['info']
    print(collection)
    find = db.collection.find()
    print(find)
