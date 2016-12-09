import discord
from discord.ext import commands

class myFF:
    """Meh"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ff(self):
        """Butts"""

        #Your code will go here
        await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(myFF(bot))
