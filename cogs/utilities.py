import discord
from discord.ext import commands

class Utilities():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reverse",
            description="Reverse a string",
            brief="Reverse a string",
            aliases=["r", "rev"])
    async def reverse(self, text : str):
        await self.bot.say("```%s```" % text[::(-1)])

    @commands.command(name="wordcount",
            description="Count number of words in a text",
            brief="Word Count - total number of words in supplied text",
            aliases=["wc"])
    async def wordcount(self, text : str):
        await self.bot.say("```%s```" % len(text.split(" ")))


    @commands.command(name="length",
            description="Total number of characters in a text",
            brief="Count the total number of characters in supplied text",
            aliases=["len", "count", "c"])
    async def length(self, text : str):
        await self.bot.say("```%s```" % len(text))

