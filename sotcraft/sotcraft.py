import discord
from discord.ext import commands
import aiohttp
import requests
import simplejson

class usersOnline:
    """Finds users that are online in Sotcraft"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sotcraft(self):

        #Your code will go here
        url = 'https://mcapi.ca/query/47.186.163.211/extensive'
        r = requests.get(url)
        for item in r.json():
            print['list']

def setup(bot):
    bot.add_cog(usersOnline(bot))
