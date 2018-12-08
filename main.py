import sys
sys.path.insert(0, "./cogs")

from hashing import Hashing
from encoding import Encoding
from ciphers import Ciphers
from utilities import Utilities
from ctfs import CTFs
from fun import Fun

from discord.ext.commands import Bot
import discord
import asyncio
import os

#app_id = '519995591359594538'
TOKEN = os.environ["DISCORD_TOKEN"]
BOT_PREFIX = (".", "dad ")

client = Bot(command_prefix=BOT_PREFIX)

client.add_cog(Hashing(client))
client.add_cog(Encoding(client))
client.add_cog(Ciphers(client))
client.add_cog(Utilities(client))
client.add_cog(CTFs(client))
client.add_cog(Fun(client))

@client.event
async def on_ready():
    print("--------Logged in as " + client.user.name + "-----------")

@client.event
async def on_message(message):
    # print("Command received: " + str(message.content))
    await client.process_commands(message)

async def list_servers():
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game(name="Despacito 3 feat. PewDiePie", url="https://www.youtube.com/watch?v=Vp1R4bb3FMw"))

client.loop.create_task(list_servers())
client.run(TOKEN)
