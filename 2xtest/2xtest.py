import discord
from discord.ext import commands
import urllib.request
import re
import time
import datetime
import traceback
from datetime import datetime, timedelta

class twoXcog:

    """Finds the next 2x time"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test2x(self):

def setup(bot):
    bot.add_cog(twoXcog(bot))
