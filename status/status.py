import discord
from discord.ext import commands
import socket


class Sstatus:
    """Finds the current in-game server status"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverstatus(self):


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex(('8.31.99.143', 8484))

        if result == 0:
            await self.bot.say('Server responded')
        s.close()


def setup(bot):
    bot.add_cog(Sstatus(bot))
