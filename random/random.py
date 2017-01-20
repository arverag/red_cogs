import discord
from discord.ext import commands
from random import randrange, uniform

class Randomcog:
    """Replies with random number"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def random(self):

        #Your code will go here
        rando = randrange(0,9)
        try:
            await self.bot.say('Random number - ' + rando)
        except:
            await self.bot.say("Couldn't give random number")

def setup(bot):
    bot.add_cog(Randomcog(bot))
