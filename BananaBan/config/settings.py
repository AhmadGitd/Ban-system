import os
from dotenv import load_dotenv

load_dotenv()

#application# for ban bruger på discord
#confirmation for at brugeren kan komme ind i sytemeet
MAXIMUM_CONFIRMATION_CHECKS = 20

#
BANK_IP = '54.183.16.194'
BANK_PROTOCOL ='http'
BOT_ACCOUNT_NUMBER =""

#Discord
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

#Mongo
MONGO_DB_NAME = 'BananaBanDB'
MONGO_HOST = 'localhost'
MONGO_PORT = '27817'