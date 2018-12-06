import discord
from discord.ext import commands

import hashlib

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
