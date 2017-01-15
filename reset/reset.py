import discord
from discord.ext import commands
import aiohttp
import datetime

class Resetcog:
    """Responds with the time until the next server reset."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reset(self):

        #Your code will go here
        _3AM = datetime.time(hour=3)
        _FRI = 4 # Monday=0 for weekday()

        def next_friday_3am(now):
            now += datetime.timedelta(days=7)
            if now.time() < _3AM:
                now = now.combine(now.date(),_3AM)
            else:
                now = now.combine(now.date(),_3AM) + datetime.timedelta(days=1)
                return now + datetime.timedelta((_FRI - now.weekday()) % 7)

        if __name__ == '__main__':
            start = datetime.datetime.now()
            for i in xrange(7*24*60*60):
                now = start + datetime.timedelta(seconds=i)
                then = next_friday_3am(now)
                assert datetime.timedelta(days=7) < then - now <= datetime.timedelta(days=14)
                assert then.weekday() == _FRI
                assert then.time() == _3AM
                
                try:
 		            await self.bot.say('Time until server reset - ' + i)
       			except:
            	    await self.bot.say("Couldn't load server reset time.")

def setup(bot):
    bot.add_cog(Resetcog(bot))
