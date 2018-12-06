import sys
sys.path.insert(0, "./cogs")

from hashing import Hashing
from encoding import Encoding
from ciphers import Ciphers
from utilities import Utilities

from discord.ext.commands import Bot
import asyncio
import os

#app_id = '519995591359594538'
TOKEN = os.environ["DISCORD_TOKEN"]
BOT_PREFIX = (".", ":")

client = Bot(command_prefix=BOT_PREFIX)

client.add_cog(Hashing(client))
client.add_cog(Encoding(client))
client.add_cog(Ciphers(client))
client.add_cog(Utilities(client))

@client.event
async def on_ready():
    print("--------Logged in as " + client.user.name + "-----------")


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("---------------")
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)
