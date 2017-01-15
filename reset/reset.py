import discord
from discord.ext import commands
import aiohttp
import datetime

class Resetcog:
    """Responds with the time until the next server reset."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def time(self):

        #Your code will go here
        today = datetime.date.today()
        friday = today + datetime.timedelta( (3-today.weekday()) %7+1)
        
        servertime = datetime.datetime.utcnow().strftime("%a, %b %d at %H:%M:%S %Z")
        try:
            await self.bot.say('GMS server time is - ' + servertime)
        except:
            await self.bot.say("Couldn't load server time.")

def setup(bot):
    bot.add_cog(Resetcog(bot))
