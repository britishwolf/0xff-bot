import discord
from discord.ext import commands

import requests
import json
from dateutil.parser import parse

class CTFs():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="upcoming",
        description="List upcoming CTFs",
        brief="List upcoming CTF competitions",
        aliases=["uc"])
    async def upcoming(self):
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"}
        r = requests.get("https://ctftime.org/api/v1/events/?limit=100&start=1544059804&online=1&restrictions=0", headers=headers).text
        r = json.loads(r)
        em = discord.Embed(title="Upcoming CTFs", type="rich", color=4622836)
        for ctf in r:
            ctfStart = parse(ctf["start"]).strftime("%d-%m-%Y %H:%M")
            em.add_field(name=ctf["title"], value=ctfStart, inline=False)
        await self.bot.say(embed=em)


