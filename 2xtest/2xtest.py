import discord
from discord.ext import commands
import urllib2
from bs4 import BeautifulSoup

class twoX:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test2x(self):
        """This does stuff!"""

        #Your code will go here
        website = 'https://e8tdwagy36.execute-api.us-west-2.amazonaws.com/prod/getTimeUntilNextEvent'
        page = urllib2.urlopen(website)

        soup = BeautifulSoup(page, 'html.parser')

        prebox = soup.find('pre')

        twoxtime = prebox.text.strip()

        await self.bot.say(twoxtime)

def setup(bot):
    bot.add_cog(twoX(bot))
