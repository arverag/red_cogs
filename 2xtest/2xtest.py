import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class twoX:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test2x(self):
        """This does stuff!"""

        #Your code will go here
        website = 'http://nintendo.com/'
        r = requests.get(website)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        for datapull in soup.find_all('a', attrs={'class':'change-region'}):
            await self.bot.say(datapull.text)

def setup(bot):
    bot.add_cog(twoX(bot))
