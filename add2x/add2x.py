import discord
import requests
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks
from __main__ import user_allowed


class new2x:

    """Finds the next 2x time"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    @checks.mod_or_permissions(administrator=True)
    async def add2x(self, ctx, date: str=None):

        url = "https://e2tg4byzod.execute-api.us-west-2.amazonaws.com/prod/setEventDay?date="
        combined = url + date
        headers = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(combined, headers=headers)
        await self.bot.say(date + " has been added to the 2x list.");
        
    @commands.command(pass_context=True)
    @checks.mod_or_permissions(administrator=True)
    async def del2x(self, ctx, date: str=None):

        url = "https://8f9h5yxd20.execute-api.us-west-2.amazonaws.com/prod/unsetEventDay?date="
        combined = url + date
        headers = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(combined, headers=headers)
        await self.bot.say(date + " has been removed to the 2x list.");

def setup(bot):
    bot.add_cog(new2x(bot))
