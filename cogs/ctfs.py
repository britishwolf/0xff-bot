import discord
from discord.ext import commands

import requests
import time
from dateutil.parser import parse

class CTFs():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="upcoming",
        description="List upcoming CTFs",
        brief="List upcoming CTF competitions",
        aliases=["uc"])
    async def upcoming(self):
        url_template = "https://ctftime.org/api/v1/events/?limit=15&start=%s&online=1&restrictions=0"
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"}

        r = requests.get(url_template % str(int(time.time())), headers=headers).json()

        em = discord.Embed(title="**Upcoming CTFs**", description="CTF competitions in the near future (displaying max. 15 results)", type="rich", color=4622836)

        title_template="%s [%s]"

        for ctf in r:
            if ctf["location"] == "":
                ctfStart = parse(ctf["start"]).strftime("%d-%m-%Y %H:%M")
                em.add_field(name=title_template % (ctf["title"], ctf["url"]), value=ctfStart, inline=False)
        em.set_footer(text="Generated on: " + str(int(time.time())))
        await self.bot.say(embed=em)


