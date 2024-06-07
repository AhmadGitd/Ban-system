from pymongo import MongoClient

def GetDb():
    client = MongoClient('localhost:27017')
    db = client.BananaBanDB
    print("\n[ * ] Connected to DB\n")
    return db

def GetFindUser(db, userId):
    return db.userinformation.find_one(userId, {'_id': 0})

def AddUser(db, userInfo):
    db.userinformation.insert_one(userInfo)
    return "[ + ] User added!"

def GetBannedUser(db, userId):
    return db.banned_users.find_one(userId, {'_id': 0})

def AddBannedUser(db, userInfo):
    db.banned_users.insert_one(userInfo)
    return "[ + ] User banned!"

def DeleteUser(db, userId):
    return db.banned_users.delete_one(userId)

def UpdateBannedUser(db, oldData, newData):
    db.banned_users.update_one(oldData, {"$set": newData})
    return "200"
