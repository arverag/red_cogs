import discord
from discord.ext import commands

class new2x:

    """Finds the next 2x time"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def add2x(self, ctx, date: str=None):

        author = ctx.message.author
        author_channel = ctx.message.channel
        sentmsg = ctx.message


        await self.bot.say('Message: {}'.format(date));

def setup(bot):
    bot.add_cog(new2x(bot))
