import discord
from discord.ext import commands

import requests

import hashlib
import os
import re

class Hashing():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="md5",
            description="Calculates MD5 value of a string",
            brief="MD5 hash")
    async def md5(self, input_string : str):
        try:
            h = hashlib.md5()
            h.update(input_string.encode("utf-8"))
            output = h.hexdigest()
            await self.bot.say("```%s```" % output)
        except:
            await self.bot.say("An error occured!")


    @commands.command(name="sha256",
            description="Calculates SHA256 value of a string",
            brief="SHA256 hash")
    async def sha256(self, input_string : str):
        try:
            h = hashlib.sha256()
            h.update(input_string.encode("utf-8"))
            output = h.hexdigest()
            await self.bot.say("```%s```" % output)
        except:
            await self.bot.say("An error occured!")

    @commands.command(name="sha1",
            description="Calculates SHA1 value of a string",
            brief="SHA1 hash")
    async def sha1(self, input_string : str):
        try:
            h = hashlib.sha1()
            h.update(input_string.encode("utf-8"))
            output = h.hexdigest()
            await self.bot.say("```%s```" % output)
        except:
            await self.bot.say("An error occured!")

    @commands.command(name="crack",
            description="Crack a hash using hashes.org",
            brief="Crack a hash",
            alias=["c"])
    async def crack(self, input_hash : str):
        pattern = re.compile("^[0-9a-fA-F]*$")
        if re.match(pattern, input_hash) is None:
            await self.bot.say("Invalid hash format!")
            return

        hashes_token = os.environ["HASHES_TOKEN"]
        url_template = "https://hashes.org/api.php?key=%s&query=%s"
        r = requests.get(url_template % (hashes_token, input_hash)).json()

        if not r["status"] == "success":
            await self.bot.say("An error occured!")
            return

        if r["result"][input_hash] is None:
            await self.bot.say("```Unknown hash [%s]```" % input_hash)
            return

        em = discord.Embed(title="**Hash cracked!**", description=input_hash, type="rich", color=107273)
        em.add_field(name="Plaintext", value=r["result"][input_hash]["plain"], inline=False)
        em.add_field(name="Plainhex", value=r["result"][input_hash]["hexplain"], inline=False)
        em.add_field(name="Algorighm", value=r["result"][input_hash]["algorithm"], inline=False)
        em.set_footer(text="Service provided by https://hashes.org/")

        await self.bot.say(embed=em)

