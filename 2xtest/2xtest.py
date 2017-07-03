import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import re

class twoX:
    """Checks Boardwalks site for 2x times!"""

    def __init__(self, bot):
        self.bot = bot
        self.green = discord.Color.green()
        self.orange = discord.Color.orange()
        self.red = discord.Color.red()
        self.blue = discord.Color.blue()

    @commands.command()
    async def next2x(self):
        """Checks current 2x status"""

        #Your code will go here
        website = 'https://kp8h6rdrwl.execute-api.us-west-2.amazonaws.com/prod/getTimeUntilNextEvent'
        r = requests.get(website)
        soup = BeautifulSoup(r.text, 'lxml')
        for datapull in soup.find_all('body'):
            if "nope" in datapull.text:
                embed = discord.Embed(title="**I don't think 2x is scheduled.**", color=self.red)
                await self.bot.say(embed=embed)
            elif "!" in datapull.text:
                newval = re.sub(r'!', "", datapull.text)
                await self.bot.say("2x is active for another __**" + newval + "!**__")
                pulledtext = ("__**" + newval + "**__ left!")
                embed = discord.Embed(title=':tada: **2x is active!** :tada:', description=pulledtext, color=self.green)
                await self.bot.say(embed=embed)
            else:
                website2 = 'https://ijgfbhygk9.execute-api.us-west-2.amazonaws.com/prod/getEventTimes'
                r2 = requests.get(website2)
                soup2 = BeautifulSoup(r2.text, 'lxml')
                for datapull2 in soup2.find_all('body'):
                pulledtext2 = datapull2.text
                embed2 = discord.Embed(title='**2x Schedule**', description=pulledtext2, color=self.orange)
                pulledtext = datapull.text
                embed = discord.Embed(title='**The next 2x is scheduled in:**', description=pulledtext, color=self.orange)
                await self.bot.say(embed=embed)
                await self.bot.say(embed=embed2)
    
    @commands.command()
    async def check2x(self):
        """Displays known 2x dates and times"""
        
        website = 'https://ijgfbhygk9.execute-api.us-west-2.amazonaws.com/prod/getEventTimes'
        r = requests.get(website)
        soup = BeautifulSoup(r.text, 'lxml')
        for datapull in soup.find_all('body'):
            pulledtext = datapull.text
            embed = discord.Embed(title='**2x Schedule**', description=pulledtext, color=self.orange)
            await self.bot.say(embed=embed)
                
def setup(bot):
    bot.add_cog(twoX(bot))
