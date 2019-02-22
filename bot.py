from instagram import Instagram
import discord
from discord.ext import commands
import sqlite3
import asyncio
from discord.utils import get
TOKEN = 'BOT TOKEN HERE'
description = ''''''
bot = commands.Bot(command_prefix='?', description=description)
connection=sqlite3.connect('instagram')
cursor=connection.cursor()
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
   if message.content.startswith('!insta'):
       names=message.content.split(' ')[1:]
       for name in names:
           try:
               bio=Instagram(name).bio
               cursor.execute('''INSERT INTO bios VALUES(
                                ?,
                                ?
               );''',(name,bio))
               connection.commit()
               await bot.send_message(message.channel,'%s was added to the monitoring '%(name))

           except:
               await bot.send_message(message.channel,"Sorry I couldn't find a user by the name %s"%(name))

   elif message.content.startswith('!remove'):
       names=message.content.split(' ')[1:]
       for name in names:
           cursor.execute('''DELETE FROM bios WHERE name=?;''',(name,))
           await bot.send_message(message.channel,'%s was removed successfully'%name)
bot.run(TOKEN)