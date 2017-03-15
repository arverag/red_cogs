import discord
from discord.ext import commands
import aiohttp
import json
import urllib
from urllib.request import urlopen
url = "https://mcapi.ca/query/47.186.163.211/extensive"

class usersOnline:
    """Finds users that are online in Sotcraft"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sotcraft(self):

        #Your code will go here
        response = urllib.urlopen(url)    
        data = json.loads(response.read())
        onlineUsers - data["list"]
        try:
            await self.bot.say('Users Online: ' + onlineUsers)
        except:
            await self.bot.say("An error occurred")

def setup(bot):
    bot.add_cog(usersOnline(bot))
