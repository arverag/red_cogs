import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import re

class twoX:
    """Checks Boardwalks site for 2x times!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def next2x(self):
        """This does stuff!"""

        #Your code will go here
        website = 'https://kp8h6rdrwl.execute-api.us-west-2.amazonaws.com/prod/getTimeUntilNextEvent'
        r = requests.get(website)
        soup = BeautifulSoup(r.text, 'lxml')
        for datapull in soup.find_all('body'):
            if "nope" in datapull.text:
                await self.bot.say("I don't think 2x is scheduled.")
            elif "!" in datapull.text:
                newval = re.sub(r'!', "", datapull.text)
                await self.bot.say("2x is active for another __**" + newval + "!**__")
            else:
                await self.bot.say("The next 2x is scheduled in: " + datapull.text + ".")

def setup(bot):
    bot.add_cog(twoX(bot))
