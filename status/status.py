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
        t = time.clock()
        result = s.connect_ex(('8.31.99.143', 8484))

        if result == 0:
            elapsed_time = time.clock() - t
            await self.bot.say('GMS Login Server responded in ' + format(elapsed_time, '.3f') + ' seconds :thumbsup:')
        else:
            await self.bot.say('The GMS Login Server did not respond in time :triumph: ')
        s.close()
        
class RBstatus:
    """Finds the current in-game server status"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rebootstatus(self):


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        t = time.clock()
        result = s.connect_ex(('8.31.99.161', 8585))

        if result == 0:
            elapsed_timeRB = time.clock() - t
            await self.bot.say('Reboot Channel 1 responded in ' + format(elapsed_timeRB, '.3f') + ' seconds :thumbsup:')
        else:
            await self.bot.say('Reboot Channel 1 did not respond in time :triumph: ')
        s.close()


def setup(bot):
    bot.add_cog(Sstatus(bot))
    bot.add_cog(RBstatus(bot))
