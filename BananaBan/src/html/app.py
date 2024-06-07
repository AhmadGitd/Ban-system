<<<<<<< HEAD
import collections
import os
import re
=======
<<<<<<< Updated upstream
import os, jsonify
>>>>>>> 1be38031174610adad7f46c1bfb84216a4cec70e
from datetime import datetime
from dis import dis
from hashlib import scrypt
from multiprocessing.sharedctypes import Value
from database import *
import bcrypt
from flask import jsonify
from bson.json_util import dumps, loads
from flask import (Flask, json, redirect, render_template, request,
                   send_from_directory, session, url_for)
from genericpath import exists
from pymongo import MongoClient

############################################################################
#                                                                          #
#                            FLASK Setup                                   #
#                                                                          #
############################################################################
=======
from codecs import StreamReaderWriter
import os, datetime
from pickle import TRUE
from flask import Flask, render_template, request, json, send_from_directory, url_for
>>>>>>> Stashed changes

app = Flask(__name__, static_url_path='/static')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.secret_key = b'jiF189Vr703d6qWCVY3'

@app.route('/favicon.ico') 
def Favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

############################################################################
#                                                                          #
#                            Route Endpoints                               #
#                                                                          #
############################################################################
############################################################################
#                                                                          #
#                            Kode omkring adgang til hjemmeside            #
#                                                                          #
############################################################################
def IsUserLoggedIn():
    return "email" in session

<<<<<<< HEAD
def UserExists(db, field, value):
    return GetFindUser(db, {field: re.compile('^' + value + '$', re.IGNORECASE)}) is not None

@app.route('/', methods=['POST', 'GET']) 
def Index():
    db = GetDb()
    message = ""  
    if IsUserLoggedIn():
        return redirect(url_for("LoggedIn"))
    if request.method == "POST":
        username = request.form.get("fuldnavn")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
       
        if UserExists(db, "fuldnavn", username):
            message = 'There is already a user by that name'
            return render_template('regis.html', message=message)
        if UserExists(db, "email", email):
            message = 'There is already an email by that name'
            return render_template('regis.html', message=message)
        if password1 != password2:
            message = 'Passwords should match'
            return render_template('regis.html', message=message)
        else:
            hashedPassword = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            userInput = {'name': username, 'email': email, 'password': hashedPassword}
            AddUser(db, userInput)
            userData = GetFindUser(db, {"email": re.compile('^' + email + '$', re.IGNORECASE)})
            newEmail = userData["email"]
            return render_template('loggedin.html', email=newEmail), {"Refresh": "3; url=login"}
    return render_template('regis.html')
=======
#@app.route('/')
#def index():
  #  return render_template('index.html')

<<<<<<< Updated upstream
# @app.route('/')
# def landing_page():
>>>>>>> 1be38031174610adad7f46c1bfb84216a4cec70e

@app.route('/login',  methods=["POST", "GET"])
def Login():
    db = GetDb()
   
    message = 'Please login'
    if "email" in session:
        return redirect(url_for("LoggedIn"))
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        emailFound = GetFindUser(db,{"email": re.compile('^' + email + '$', re.IGNORECASE)})
        if emailFound:
            emailVal = emailFound['email']
            passwordCheck = emailFound['password']

            if bcrypt.checkpw(password.encode('utf-8'), passwordCheck):
                session["email"] = emailVal
                return render_template('loggedin.html', email=emailVal),{"Refresh": "2; url=index"} 
            else:
                if "email" in session:
                    return redirect(url_for("LoggedIn"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = "Email ikke fundet"
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route('/loggedin')
def LoggedIn():
    if "email" in session:
        email = session["email"]
        return render_template('loggedin.html', email=email)
    else:
        return redirect(url_for("Login"))

@app.route('/loggedout', methods=["POST", "GET"])  
def Logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("loggedout.html")
    else:
        return render_template("regis.html")

@app.route('/index')
def Home():
    return render_template("index.html")

############################################################################
#                                                                          #
#                            Kode til programmets funktioner               #
#                                                                          #
############################################################################
@app.route('/ban',  methods=['GET'])
def BanUser():
    return render_template('ban.html')


@app.route('/ban', methods=['POST'])
def BanUserPost():
    db = GetDb()
    if  GetBannedUser(db,{'DiscordID': re.compile('^' + request.form['discordID'] + '$', re.IGNORECASE)}) or GetBannedUser(db,{'SteamID': re.compile('^' + request.form['steamID'] + '$', re.IGNORECASE)}):
        disId = GetBannedUser(db,{'DiscordID' : re.compile('^' + request.form['discordID'] + '$', re.IGNORECASE)})
        stemId =  GetBannedUser(db,{'SteamID' : re.compile('^' + request.form['steamID'] + '$', re.IGNORECASE)})
        
        
        return render_template('find.html', value=disId or stemId, banned_true=True)  # Fejl:1# redirect api endpoint til find #
    else:
        steamId = request.form['steamID']
        discordId = request.form['discordID']
        reason = request.form['reason']
        server = request.form['server']
        timeBanned = datetime.now() 
        userInfo = json.dumps({'SteamID': steamId,
                                'DiscordID': discordId,
                                'Reason': reason,
                                'Server' : server,
                                'TimeStamp': timeBanned
                                }, indent = 5)
        
        print(userInfo)
        AddBannedUser(db, json.loads(userInfo))
        return render_template('ban.html', value=discordId, banned_true=True)

@app.route('/find')
def FindUser():  
    return render_template('find.html')

@app.route('/find', methods=['POST'])
def FindUserPost():
    data = GetDb()
    username = request.form['username']
    discordId = FindUserByUsername(data, username, 'DiscordID')
    steamId = FindUserByUsername(data, username, 'SteamID')
   
    if discordId or steamId:
        return render_template('find.html', value=discordId or steamId, banned_true=True)
    else:
        return render_template('find.html', value="Kan ikke finde ham", banned_true=True)

def FindUserByUsername(db, username, identifier):
    return GetBannedUser(db, {identifier : re.compile('^' + username + '$', re.IGNORECASE)})

    
############################################################################
#                                                                          #
#                            API Endpoints                                 #
#                                                                          #
############################################################################

@app.route('/api/v1/find', methods=['POST'])
def FindUserApi():
    db = GetDb()
    username = request.form['username']
    steamId = GetBannedUser(db,{'SteamID' : re.compile('^' + username + '$', re.IGNORECASE)})
    discordId = GetBannedUser(db,{'DiscordID' : re.compile('^' + username + '$', re.IGNORECASE)}) 
    
   
    if steamId and discordId =="null":
        print("He Steam ID exist")
        return "User steam ID exist can use the find"
        #return dumps(discordId)
    if steamId and discordId !="null":
        print("Not steam id exist")
        return dumps(steamId) or dumps(discordId)
    
        return "User discord ID exist can use the find"
    if discordId != "null":
        print("Not discord id exist")
        return dumps(discordId)
   
   

@app.route('/api/v1/banuser', methods=['POST'])
<<<<<<< HEAD
def BanUserApi():
   
    db = GetDb()
    userInfo = request.get_json()
    formatted = json.loads(userInfo)
    AddBannedUser(db, formatted) 
=======
def ban_user_api():
    data = request.get_json(cache=True)
    print(data)
=======
#@app.route('/', methods=['POST'])
#def my_form_post():
    #text = request.form['textbox']
    #processed_text = text.upper()
    #return print ('ddasd')
    #return render_template('index.html', value=processed_text)

#@app.route('/api/v1/postinfo', methods=['POST'])
#def send():
  #  data = request.get_json(cache=True)
   
   # print(data)
    # DoSomethingWithData(data)
    #return data,"data collected"#jsonify(data)
>>>>>>> Stashed changes
>>>>>>> 1be38031174610adad7f46c1bfb84216a4cec70e
    
    return "User er banned nu "

<<<<<<< HEAD
@app.route('/api/v1/delete', methods=['POST'])
def UnbanUserApi():    
    db = GetDb()
    username = request.form['username']
    discordId = GetBannedUser(db,{"DiscordID": re.compile('^' + username + '$', re.IGNORECASE)}) 
    steamId = GetBannedUser(db,{"SteamID": re.compile('^' + username + '$', re.IGNORECASE)})
    
    print(GetBannedUser(db,{"DiscordID": re.compile('^' + username + '$', re.IGNORECASE)}))
    if discordId != None:
        
        DeleteUser(db,{"DiscordID": re.compile('^' + username + '$', re.IGNORECASE)})
        print("User er slettet")
        return " slettet"
    if steamId != None:
        DeleteUser(db,{"SteamID": re.compile('^' + username + '$', re.IGNORECASE)}) 
        print("User er slettet")
        return " slettet"
    else:
        return " findes ikke"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
=======
############################################################################
#                                                                          #
#                            DB Functions                                  #
#                                                                          #
############################################################################   
 
def get_db():
    client = MongoClient('localhost:27017')
    db = client.BananaBanDB
    print("\n[ * ] Connected to DB\n")
    return db

<<<<<<< Updated upstream
def add_banned_user(db, user_info):
    db.banned_users.insert_one(user_info)
    print("\n[ + ] User banned!\n")
    #return "[ + ] User banned!"
    
def get_banned_user(db):
    return db.banned_users.find_one()
=======
#def DoSomethingWithData(data):
    #return data

#def userExist():
    #while TRUE:
     #   DiscordName = 
      #  SteamID =
      #if not DiscordName or not SteamID:
       #     print ("This username dosent exist.")
        #else DiscordName or SteamID in MongolDB
         #   print.mongolDB.info()

#def UserExist():
    #for discordname in ('bar', 'foo'):
     #   cursor.execute("SELECT rowid FROM compentents WHERE discordname = ?", (discordname,))
      #  data=cursor.fetchall()
       # if len(data)==0:
        #    print('This user cant be find %s'%discordname)
        #else:
         #   print('User %s found with the info %s'%(discordname,','.join(map(str, next(zip(*data))))))


# while True:
#    print.Info()
#Var discordName
#Var SteamID
#var datetime.date
#var string reason 
#var server
>>>>>>> Stashed changes
>>>>>>> 1be38031174610adad7f46c1bfb84216a4cec70e
