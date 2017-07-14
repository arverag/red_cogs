import discord
import requests
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks
from __main__ import user_allowed


class textme:

    """Texts Zelkova"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    @checks.mod_or_permissions(administrator=True)
    async def text(self, ctx, phmessage: str=None):

        url = "https://freetxtapi.com"
        pnumber = ""
        headers = {'user-agent': 'Mozilla/5.0'}
        r = requests.post('https://freetxtapi.com', {'phone': pnumber, 'message': phmessage}, headers=headers)

        await self.bot.say("Message has been sent");

def setup(bot):
    bot.add_cog(textme(bot))
