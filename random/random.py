import discord
from discord.ext import commands
from random import randint

class Randomcog:
    """Replies with random number"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def time(self):

        #Your code will go here
        rando = (randint(0,9))
        try:
            await self.bot.say('Random number - ' + rando)
        except:
            await self.bot.say("Couldn't give random number")

def setup(bot):
    bot.add_cog(Timecog(bot))
