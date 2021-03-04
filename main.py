# Work with Python 3.6
import discord
import os 
from keepalive import keep_alive
import requests
import json
from weather import *
import youtube_dl

client = discord.Client()
command_prefix = "c."
TOKEN_API =os.getenv('TOKEN_API')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('hola'):
        await message.channel.send('Callate wey ')
    if message.content.startswith("gg"):
      await message.channel.send("WP GG Yoking We Shillin Solobolo")
    #Weather API
    
    if message.author != client.user and message.content.startswith(command_prefix):

      if len(message.content.replace(command_prefix,''))>=1:

        location = message.content.replace(command_prefix, '').lower()
        url= f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={TOKEN_API}&units=metric'
        try: 
          data = parse_data(json.loads(requests.get(url).content)['main'])
          await message.channel.send(embed=weather_message(data,location))
        except KeyError:
            await message.channel.send(embed=error_message(location))
      
          

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='c.[location]'))
  print('Logged in as ')
  print(client.user.name)
  print(client.user.id)
  print('------')
keep_alive()
client.run(os.getenv('TOKEN'))