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

        texts = ["%s drooped his soap in a prison. Whoops!",
                "%s is currently being banged by some hunky guys.",
                "%s has his orifices full of tasty meat",
                "Daddybot is having an intercourse with %s",
                "%s is being thoroughly satisfied."]

        message = random.choice(texts)
        if person is None:
            await self.bot.say(message % ctx.message.author.mention)
            return
        
        await self.bot.say(message % person.mention)
        # await self.bot.say("hugs {}".format(ctx.message.author.mention))
