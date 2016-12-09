import discord
from discord.ext import commands

class myFF:
    """Meh"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ff(self):

        #Your code will go here
        await self.bot.say(":saughting:")

def setup(bot):
    bot.add_cog(myFF(bot))
