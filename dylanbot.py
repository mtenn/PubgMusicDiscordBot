# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:03:14 2018

@author: Mike
"""

import discord
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
        print("Bot Online!")
        print("Name: ()".format(client.user.name))
        print("ID: ()".format(client.user.id))
        
@client.command(pass_context=True)
async def ping(ctx) :
    await client.say("Pong!")
    
async def dylansucks(ctx) :
    await client.say("Pong!")
    
    
client.run("NDExMzA3MjM0OTkyMDYyNDY1.DV53sg.D_PfR2WyWs7MSgGA3TME4JMJA2s") 


# pubgtracker api key: TRN-Api-Key: 3810ed2c-1f0b-477a-b29d-06d57557cd77   