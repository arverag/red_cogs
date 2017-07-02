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
        website = 'http://imzelkova.com/twitch'
        page = requests.get(website)
        soup = BeautifulSoup(page.text, 'html.parser')
        for testthing in soup.find_all('span'):
            await self.bot.say(testthing.text)

def setup(bot):
    bot.add_cog(twoX(bot))
