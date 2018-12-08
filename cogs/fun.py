import random
import binascii

import discord
from discord.ext import commands

class Fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fuck",
        description="Have sexual intercourse with someone",
        brief="Have a quickie with someone",
        aliases=["consentisnotrape"],
        pass_context=True)
    async def fuck(self, ctx, person : discord.User=None):

        with open("cogs/pleasures.txt", "r") as f:
            texts = f.readlines()
        message = random.choice(texts)
        if person is None:
            await self.bot.say(message % ctx.message.author.mention)
            return
        
        await self.bot.say(message % person.mention)
        # await self.bot.say("hugs {}".format(ctx.message.author.mention))

    @commands.command(name="howgay",
        description="Measure someone's gayness",
        brief="Measure someone's gayness",
        aliases=["howfag"],
        pass_context=True)
    async def gay(self, ctx, person : discord.User=None, hax : int=-1):

        if person is None:
            person = ctx.message.author

        percentage = None 
        
        if hax > 100:
            percentage = 100
            person = ctx.message.author
        elif hax < 0:
            percentage = binascii.crc32(str.encode(person.name)) % 100
        else:
            percentage = hax

        await self.bot.say(person.mention + " is %s percent gay!" % str(percentage))
