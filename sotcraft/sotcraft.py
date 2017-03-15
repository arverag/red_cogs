import discord
from discord.ext import commands
import aiohttp
import requests

class usersOnline:
    """Finds users that are online in Sotcraft"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sotcraft(self):

        #Your code will go here
        url = 'https://mcapi.ca/query/47.186.163.211/extensive'
        response = requests.get(url, verify=True) #Verify is check SSL certificate
        data = response.json()
        onlineUsers = data[0]['list']
        try:
            await self.bot.say('```'+ onlineUsers +'```')
        except:
            await self.bot.say("An error occurred")

def setup(bot):
    bot.add_cog(usersOnline(bot))
