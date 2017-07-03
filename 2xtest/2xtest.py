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
        """Checks current 2x status"""

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

    async def check2x(self):
        """Displays known 2x dates and times"""
        
        website = 'https://ijgfbhygk9.execute-api.us-west-2.amazonaws.com/prod/getEventTimes'
        r = requests.get(website)
        soup = BeautifulSoup(r.text, 'lxml')
        for datapull in soup.find_all('body'):
            await self.bot.say(datapull.text)
                
def setup(bot):
    bot.add_cog(twoX(bot))
