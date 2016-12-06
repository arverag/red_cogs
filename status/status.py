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
        start = time.clock()
        result = s.connect_ex(('127.0.0.1', 3306))

        if result == 0:
            await self.bot.say('Server responded in ', time.clock()-start ,' seconds')
        s.close()
        else result == 1:
            await self.bot.say("Server no respondo")
        s.close()               
        
def setup(bot):
    bot.add_cog(Sstatus(bot))
