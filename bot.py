import discord
from discord.ext import commands
from discord.ext.commands.core import command

Bot = commands.Bot(command_prefix='')

@Bot.event
async def on_ready():
  print("Hazırım")

@Bot.command(aliases=["Sa", "Sea", "sa"])
async def sea(msg):
    await msg.send('Aleyküm Selam')
@Bot.command()
async def link(msg):
    await msg.send('https://www.youtube.com/channel/UCQPWPuU8_z1gP96YICcRtfQ')
@Bot.command()
async def naber(msg):
    await msg.send('İyiyiz senden naber?')
@Bot.command()
async def Naber(msg):
    await msg.send('İyiyiz senden naber?')
@Bot.command()
async def nasılsınız(msg):
    await msg.send('İyiyiz sen nasılsın?')
@Bot.command()
async def Nasılsınız(msg):
    await msg.send('İyiyiz sen nasılsın?')
@Bot.command(aliases=["Yapımcı"])
async def yapımcı(msg):
    await msg.send('Yapımcım: Kerem Özdilsiz. Ulaşmak için İnstagram:@keremozdilsizdir')


Bot.run('')
