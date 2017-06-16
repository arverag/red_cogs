import discord
from discord.ext import commands
from collections import namedtuple
from cogs.utils.chat_formatting import escape, pagify

class new2x:

    """Finds the next 2x time"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def add2x(self, ctx, channel):

        author = ctx.message.author
        author_channel = ctx.message.channel

        def check(m):
            try:
                return (m.content)
            except:
                return False
                
        await self.bot.say(m.content);

def setup(bot):
    bot.add_cog(new2x(bot))
