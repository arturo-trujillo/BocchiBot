import discord 


color= 0xFF6500
thumbnail = "https://repl.it/@ARTUROTRUJILLO1/BocchiBot#weather.png"

key_features = {
  'temp': 'Temperatura actual',
  'feels_like' : ' Sensacion Termica',
  'temp_min': 'Temperatura minima',
  'temp_max': 'Temperatura maxima',
}

def parse_data(data):
  del data['humidity']
  del data['pressure']
  return data

def weather_message(data,location):
  location = location.title()
  message = discord.Embed(
    title= f'Vals Clima (C°)',
    description = f'Clima en {location}.',
    color=color, 
  )
  message.set_thumbnail(url ="https://pbs.twimg.com/profile_images/1173919481082580992/f95OeyEW_400x400.jpg")
  for key in data:
    message.add_field(
    name=key_features[key],
    value=str(data[key]),
    inline=False
    )
  return message

def error_message(location):
  location = location.title()
  return discord.Embed(
    title='Error',
    description=f'Ocurrio un error al obtener la informacion de {location} (Intenta escribirendo de nuevo el lugar).',
    color= color
  )
