from datetime import datetime
from email import header
from genericpath import exists
from http import client
from lib2to3.pgen2.token import EQUAL
from pickle import TRUE
import re
from tabnanny import check
from time import time
from unittest import result
from wsgiref import headers
from discord.ext import commands
import discord
import os
import random, requests, json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
intents.members = True
owners = [192444905082191872, 237252600234246144]
bot = commands.Bot(intents=intents, command_prefix='!', owner_ids=set(owners))

############################################################################
#                                                                          #
#                            Bots self handling                            #
#                                                                          #
############################################################################  
@bot.event
async def OnReady():
    await bot.change_presence(status=discord.Status.invisible)

@bot.event
async def OnCommandError(ctx, error):
    if isinstance(error, commands.errors.CheckAnyFailure):
        await ctx.send('Du har ikke den rigtig role til at udføre denne handling')

############################################################################
#                                                                          #
#                            Bots skal kunne gør                           #
#                                                                          #
############################################################################
@bot.command(name='ban',help="Give following data -> 'Reason' SteamID Server")
@commands.has_permissions(ban_members=True)
async def Ban(ctx, member: discord.Member, steamId: str, reason: str, server: str):
    
    timeBanned = GetTime()
    headers = {'Content-type': 'application/json'} 
    data = {
        "SteamID": steamId,
        "DiscordID": str(member),
        "Reason": reason,
        "Server": server,
        "TimeStamp": timeBanned
    } 
    
    jsonObject = json.dumps(data) 
    
    pattern = re.compile(r"^STEAM_[0-5]:[0-1]:[0-9]*$")
    st = re.match(pattern, steamId)
        
    username = {'username': str(member) or steamId}
    
    r = await FindUserRequest(username)
   
    if st:
        
        if r == "null":
            await ctx.send(f'Mother fuqer is banned, INFO -> \nDiscord = {member} \nSteamID = {steamId} \nReason = {reason} \nServer = {server}')
            await BanUserRequest(jsonObject, headers)
            await ctx.guild.ban(member)
              
                     
        if r != "null": 
            await ctx.send(f'he exist in the system, use the !find to get his information')
            print("user exist in db ")
           
        else:
            await ctx.send(f'steamid er ikke korrekt')
    
    if steamId == "uk":
        if r == "null": 
            await ctx.send(f'Mother fuqer is banned, INFO -> \nDiscord = {member} \nSteamID = {steamId} \nReason = {reason} \nServer = {server}')
            await BanUserRequest(jsonObject, headers)
        if r != "null":
            await ctx.send(f'discordId findes brug find')

@bot.command(name='find', help="Give following data -> 'Discord name' ")
@commands.has_permissions(ban_members=True)
async def Find(ctx, discordName: str):
    members = []

    for member in ctx.guild.members: 
        members.append(member.name + "#" + str(member.discriminator))
    
    if any(discordName in x for x in members):
         await ctx.send(f'Mother fuqer is in guild! \nDiscord ID : {discordName}')
    else:
        await ctx.send(f'Mother fuqer is not in guild! \nDiscord ID : {discordName}')
    
    data = {'username': str(discordName)}
    
    def ConvertTuple(tup):
        str = ''.join(tup)
        return str
    
    r = await FindUserRequest(data)
    f = ConvertTuple(r)    
    
    if discordName in f:
        dataDb = json.loads(f)
        json.dumps(dataDb, indent=4)
        discordId = dataDb["DiscordID"]
        steamId = dataDb["SteamID"]
        reason = dataDb["Reason"]
        server = dataDb["Server"]
        timestamp = dataDb["TimeStamp"]
        startMe = "```"
        endMe = "```"
        formatting = "json"
        
        await ctx.send(f'Mother fuqer is banned! \nDiscord ID : {discordName}')

        getInfo = f'\nMother fuqerz information:\n\nDiscord ID : "{discordId}"\nSteamID : "{steamId}"\nReason : "{reason}"\nServer : "{server}"\nTimeStamp : "{timestamp}"'
        await ctx.send(startMe + formatting + "\n" +  getInfo + endMe)
        print(getInfo)
    
    if discordName not in f:
        await ctx.send(f'Mother fuqer is not banned! \nDiscord ID : {discordName}')

@bot.command(name='slet', help="Sletter en fra database")
@commands.is_owner()
async def Delete(ctx, member: str):
    data = {'username': member}
    
    if await FindUserRequest(data) != "null":
        await ctx.send(f'bruger er slettet')
        await DeleteUserRequest(data)
    else:
        return False

@bot.command(name='update', help="updater en fra database")
@commands.is_owner()
async def Update(ctx, member: str, steamId: str, reason: str, server: str):
    
    data = {'username': member}
    data3 = {'username': steamId}
    data1 = {'username': reason}
    data2 = {'username': server}    
   
    timeBanned = GetTime()
    headers = {'Content-type': 'application/json'} 
    data4 = {
        "SteamID": steamId,
        "DiscordID": str(member),
        "Reason": reason,
        "Server": server,
        "TimeStamp": timeBanned
    } 
    
    jsonObject = json.dumps(data4) 

def GetTime():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

############################################################################
#                                                                          #
#                            API BOT REQUEST                               #
#                                                                          #
############################################################################  
async def BanUserRequest(data, headers):
    resp = requests.post(url="http://127.0.0.1/api/v1/banuser", json=data, headers=headers)
    print(resp.text)
    return "[ + ] DONE", 200

async def FindUserRequest(data):
    resp = requests.post(url="http://127.0.0.1/api/v1/find", data=data)
    print(resp.text)
    return resp.text

async def DeleteUserRequest(data):
    resp = requests.post(url="http://127.0.0.1/api/v1/delete", data=data)
    print(resp.text)
    return resp.text

async def UpdateUserRequest(data, headers):
    resp = requests.post(url="http://127.0.0.1/api/v1/update", data=data, headers=headers)
    print(resp.text)
    return resp.text

bot.run(TOKEN)
