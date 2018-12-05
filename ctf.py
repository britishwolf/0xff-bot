import discord
from discord.ext import commands

import base64
import hashlib
import urllib.parse


class CTF():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="base64",
        description="Encodes/decodes base64 (example: base64 d <string>)",
        brief="Encodes/decodes base64",
        aliases=['b64'])
    async def base64(self, mode : str, input_string : str):

        accepted_modes = ["d", "decode", "e", "encode"]
        if not mode in accepted_modes:
            await self.bot.say("Enter a valid mode!")
            return

        byted_str = str.encode(input_string)

        try:
            if mode[0] == "d":
                await self.bot.say("```%s```" % base64.b64decode(byted_str).decode('utf-8'))
            else:
                await self.bot.say("```%s```" % base64.b64encode(byted_str).decode('utf-8').replace('\n', ''))
        except:
            await self.bot.say("An error occured!")

    @commands.command(name="url",
            description="Encodes/decodes string with url encoding",
            brief="Url encoding")
    async def url(self, mode : str, input_string : str):
        accepted_modes = ["d", "decode", "e", "encode"]
        if not mode in accepted_modes:
            await self.bot.say("Enter a valid mode!")
            return
        
        try:
            if mode[0] == "d":
                input_string = input_string.replace("%20", " ")
                await self.bot.say("```%s```" % urllib.parse.unquote(input_string))
            else:
                await self.bot.say("```%s```" % urllib.parse.quote(input_string))
        except:
            await self.bot.say("An error occured!")

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



