import discord
from discord.ext import commands
import socket
import time


class Sstatus:
    """Finds the current in-game server status"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverstatus(self):


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        t = time.process_time()
        result = s.connect_ex(('8.31.99.143', 8484))

        if result == 0:
            elapsed_time = time.process_time() - t
            await self.bot.say('Server responded in ' + elapsed_time + ' seconds.')
        s.close()


def setup(bot):
    bot.add_cog(Sstatus(bot))
