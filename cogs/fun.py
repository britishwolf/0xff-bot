import random

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
