import discord
from discord.ext import commands

class Timecog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def time(self):
        """This does stuff!"""

        #Your code will go here
        url = "https://www.timeanddate.com/time/zones/pst" #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            servertime = soupObject.find(class_='ctm-tz').find('span').find(id_='hourmin0').get_text()
            await self.bot.say('GMS server time is ' + servertime)
        except:
            await self.bot.say("Couldn't load server time.")

def setup(bot):
    bot.add_cog(Timecog(bot))
