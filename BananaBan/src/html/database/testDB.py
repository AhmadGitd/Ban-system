
from cgitb import text
import collections
from dataclasses import dataclass
from datetime import date, datetime
from email import message
from http import client
from operator import imod
from optparse import check_choice
from pprint import pprint
from re import IGNORECASE, X, search
import re
from tabnanny import check
from time import time
from tkinter import Y
from typing import Text
from unittest import skip
from xml.dom.minidom import Document
from xmlrpc.client import DateTime
from bson.objectid import ObjectId
from pymongo import MongoClient





#client = MongoClient('localhost:27017')
#db = client.BBinfo
#collection = db.Banusers
#posts = db.posts


def get_db():
    
    pprint('Vælg et navn')
    unameInput = input("Enter username: ")
    unameList = {'_id.Discord_Name': unameInput}
    disnameQuery = {}
    
    #unameQuery2 = collection.find_one({'_id.Discord_Name': {'$gt': 'a'}})
    
    #check = db.Banusers.find_one({'Discord_Name': {'$gt': 'a'}}) # do something#unameInput not in unameQuery2:
    if FindUser({'Discord_Name' : re.compile('^' + unameInput + '$', re.IGNORECASE)}) is not None or  FindUser({'Steam_Id' :re.compile('^' + unameInput + '$', re.IGNORECASE)}) is not None: #collection.({ 'username': collection }, limit = 1) != 0
    
      print("Personen er banned ")
      
    else:
        pprint("Indtast discordnavn ")
        disInput = input("Enter discordname ")
       
        pprint("Indtast steamid ")
        steamInput = input("Enter steamid ")
        pprint("Indtast reason ")
        reasonInput = input("Enter reason ")
        pprint("Intast server spilleren er banned på ")
        serverInput = input("Enter server ")
        #today = datetime.datetime.today()
        time = datetime.utcnow()
        
        #d = disInput.find({'Discord_Name': collection})
        #s = steamInput.find({'Steam_id': collection})
        disName = disInput
        steamId = steamInput
        reaBan = reasonInput
        serBan = serverInput
        
        Details_info = {
                "Discord_Name": disName,
                "Steam_Id": steamId,
                "Reason_Banned": reaBan,
                "Server_Banned": serBan,
                "date" : time
                
                  
        }
        #allList = {'username': unameList}
        #unameQuery2(allList)
        # Søg felt for hjemmeside hvis bruger existere eller ikke 
    
        #check = collection.find_one({'Discord_Name': {'$gt': 'a'}})#.limit = 1 != 0
       
    
        db.Banusers.insert_one(Details_info)
       
       # Details_info = {
        #"Discord_Name": y,
        #"Steam_Id": g, 
        #"Date_Banned": "2021-04-07", 
        #"Reason_Banned": "spawner våben:modder",
        #"Server_Banned_From": "SocialRP",
        
        #}
    
    #global post_id
    
    #global get_id
    #get_id = collection.find_one()
   
    #post_id = collection.insert_one(Details_info).inserted_id
    
    return db
   
    #

#def add_country(db):
    #db.countries.insert_one({"" : "denmark"})
    
def Ban_user(db):
   return db.Banusers.find_one()

def FindUser(id): # Finder person i database
    return db.Banusers.find_one(id)

def SearchForUser():# Funktion søger efter DiscordName og steamID
    pprint('Vælg et navn')
    unameInput = input("Enter username: ")
    unameList = {'_id.Discord_Name': unameInput}
    disnameQuery = {}

    unameQuery2 = collection.find_one({'_id.Discord_Name': {'$gt': 'a'}}) # do something#unameInput not in unameQuery2:
    if FindUser({'Discord_Name' : unameInput}) or FindUser({'Steam_Id' : unameInput}): #collection.({ 'username': collection }, limit = 1) != 0
    
      print(collection.find_one({unameInput: ObjectId()}))

      
    else:
        #allList = {'username': unameList}
        #unameQuery2(allList)
        print('han findes ikke') # Søg felt for hjemmeside hvis bruger existere eller ikke 

def DoesUserExist(): # skal kunne nægte at oprette den samme user !! HVordan!
    pprint('Vælg et navn')
    uchechInput = input("Enter username: ")
    check = collection.find_one({'Discord_Name': {'$gt': 'a'}})#.limit = 1 != 0
    if check == FindUser({'Discord_Name' : uchechInput}):
        print('Han er banned')
    else:
        
   
        pprint("Indtast discordnavn ")
        disInput = input("Enter discordname ")
       
        pprint("Indtast steamid ")
        steamInput = input("Enter steamid ")
        #d = disInput.find({'Discord_Name': collection})
        #s = steamInput.find({'Steam_id': collection})
        y = disInput
        g = steamInput
        userinfo = {
                "Discord_Name": y,
                "Steam_Id": g, 
                
  
    }
    
        collection.insert_one(userinfo)
    # Noget der virker :  :  for x in posts.find({},{ "_id": 0, "Discord_Name": 1, "Reason_Banned": 1}):
    #   print(x) #virker til at finde alle data frem :

    #for x in posts.find({'Discord_Name':{'$regex': '^minijumper#2123'}}):
        #print(x) #virker til at søge efter alpca. 
        #rgx = re.compile('.*minijumper#2123.*', re.IGNORECASE)
    #for x in posts.find({'Discord_Name':{'$regex': '^Alpca#2123'}}):
     #   print(x)

     #pprint(posts.find_one({"_id": post_id})) Virker
     #pprint(posts.find_one({"_id": post_id})) Virker


    #for User in FindUser({},{ "_id": 0, "Discord_Name": 1,}):
    #print(User) #virker til ayt finde alle data frem 
    #if FindUser({'Discord_Name' : User}) or FindUser({'Steam_Id' : User}):
    #    pprint(FindUser({"_id": User}))

      #mydatabase = db.posts.find_one({'_id': ObjectId('62fd395e43dbfed990cf3194')})
      #if posts.count_documents({ 'Discord_Name': posts }, limit = 1) != 0:
       #print('forbudt')
    #for x in posts.find({},{ "_id": 0, "Discord_Name": 1, "Reason_Banned": 1}):
    #   print(x) #virker til at finde alle data frem 
    #Ban_user.find_one(collection)
    #collection.find_one({"$text": {"$search": Details_info}}).limit(10)#Den leder efter en string ogikke en objekt
    #return collection.find_one({'_id': ObjectId.__str__()}) 
    
    
    #def get(SearchForUser):
    #pprint(posts.find_one({"_id": get_id}))
    #Til = posts.find_one({'_id': ObjectId(get_id)})
    #Ban_user.find_one({"_id": Til})
 #   document = client.db.posts.find_one({'_id': ObjectId(SearchForUser)}) 
    
    
    

    
  #if db.Ban_user.collection.count_documents({'Discord_Name': details_info}, limit = 1) != 0:     
   # return details_info   
    
#https://stackoverflow.com/questions/54369494/check-if-username-already-exists-in-database-python-pymongo

    #if client.get_database({ 'BanUsers': collection }):
     #    Ban_user.send("**Error: You're already in the database**")
    #else:
     #    Ban_user.send("**Han er banned**")
        
        #mydict = { "Discord_Name": Details_info, "coin": "0", "inv": {"inv1": "", "inv2": "", "inv3": "", "inv4": "", "inv5": ""} }
        #y = client.db.posts.insert_one(mydict)
    
    #db.get_db.find({}, {"Discord_Name": 1, "Steam_Id" : 1})

    #mydatabase = db.Ban_user.find_one({'_id': ObjectId('62fd395e43dbfed990cf3194')})
    #mydatabase = client.BBinfo
    #x = db.BanUsers.find_one({'Discord_Name':'minijumper#2123'})
    #print(x)
    #pprint(db.Ban_user.find({"Discord_Name": "minijumper#2123"}))
    #rgx = re.compile('.*minijumper#2123.*', re.IGNORECASE)
    #mydatabase = db.Ban_user.find_one({'Discord_Name': rgx})
    #print (mydatabase)
    #if db.Ban_user.find({"$text": {"$search": db}}).limit(10):
     #db.Ban_user.find({'Discord_Name':{"$exists": True}}):
    #db.mydatabase.find({'$Discord_Name': mydatabase}).limit(10):S
     #   return print('its true')
    #else:
     #   return print('Usernot exist')


if __name__ == "__main__":
    client = MongoClient('localhost:27017')
    db = client.BBinfo
    BananaBan = db.Banusers
    
    #print(FindUser({"Discord_Name":"asd"}))
    get_db() 
    #add_country(db)
    #print(Ban_user(db))
    #print(get(post_id))
    #SearchForUser()
    #DoesUserExist()

    
   
   