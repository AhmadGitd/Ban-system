import collections
from http import client
from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)
db = client.test_database # BBinfo
collection = db.test_collection # banusers
import datetime
#details_info
post = {"author": "Mike", "text": "My first blog post!", "tags":["Mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id
db.list_collection_names()
['posts']
import pprint
pprint.pprint(posts.find_one({"_id": post_id}))
from bson.objectid import ObjectId
def get(post_id):
    document = client.db.collection.find_one({'_id': ObjectId(post_id)}) 
if __name__ == "__main__":
   print(get(post_id))