import discord
from discord.ext import commands
import socket
from struct import pack, unpack
    
class Sstatus:
    """Finds the current in-game server status"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverstatus(self):

        #Your code will go here
        host = socket.gethostbyname("8.31.99.143")
        port = 8484

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        packet = ""
        packet += pack('i',4)
        packet += pack('p',port)
        packet += pack('H',host)
        packet += pack('i',1)
        s.send(packet)
        serverstatus = s.recv(1024) # Recv nothing ?

        try:
            await self.bot.say('Status = ' + serverstatus)
        except:
            await self.bot.say("Couldn't load server status.")

def setup(bot):
    bot.add_cog(Sstatus(bot))
