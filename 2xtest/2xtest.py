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
                embed = discord.Embed(title="**I don't think 2x is scheduled. :thinking:**", color=self.red)
                await self.bot.say(embed=embed)
            elif "!" in datapull.text:
                newval = re.sub(r'!', "", datapull.text)
                pulledtext = ("__**" + newval + "**__ left!")
                embed = discord.Embed(title=':tada: **2x is active!** :tada:', description=pulledtext, color=self.green)
                await self.bot.say(embed=embed)
            else:
                pulledtext = (":watch: " + datapull.text + ".")
                embed = discord.Embed(title='**The next 2x is scheduled in:**', description=pulledtext, color=self.orange)
                await self.bot.say(embed=embed)
                
                website = 'https://ijgfbhygk9.execute-api.us-west-2.amazonaws.com/prod/getEventTimes'
                r = requests.get(website)
                soup = BeautifulSoup(r.text, 'lxml')
                for datapull in soup.find_all('body'):
                    pulledtext = datapull.text
                    pulledsplit = pulledtext.split()
                    pulledlen = len(pulledsplit)
                    if pulledlen > 28 :
                        timesheet = "The dumbass mod put too many 2x times on the schedule. :rage:"
                        embed = discord.Embed(title='**2x Schedule**', description=timesheet, color=self.orange)
                        await self.bot.say(embed=embed)
                    elif pulledlen >= 27 :
                        timesheet = ("```xl")
                        timesheet += ("\n")
                        timesheet += (pulledtext.split()[0] + " | " + pulledtext.split()[1] +" "+ pulledtext.split()[2] +"\n")
                        timesheet += (pulledtext.split()[3] + " | " + pulledtext.split()[4] +" "+ pulledtext.split()[5] +"\n")
                        timesheet += (pulledtext.split()[6] + " | " + pulledtext.split()[7] +" "+ pulledtext.split()[8] +"\n")
                        timesheet += ("```")
                        timesheet += ("\n")
                        timesheet += ("```xl")
                        timesheet += ("\n")
                        timesheet += (pulledtext.split()[9] + " | " + pulledtext.split()[10] +" "+ pulledtext.split()[11] +"\n")
                        timesheet += (pulledtext.split()[12] + " | " + pulledtext.split()[13] +" "+ pulledtext.split()[14] +"\n")
                        timesheet += (pulledtext.split()[15] + " | " + pulledtext.split()[16] +" "+ pulledtext.split()[17] +"\n")
                        timesheet += ("```")
                        timesheet += ("\n")
                        timesheet += ("```xl")
                        timesheet += ("\n")
                        timesheet += (pulledtext.split()[18] + " | " + pulledtext.split()[19] +" "+ pulledtext.split()[20] +"\n")
                        timesheet += (pulledtext.split()[21] + " | " + pulledtext.split()[22] +" "+ pulledtext.split()[23] +"\n")
                        timesheet += (pulledtext.split()[24] + " | " + pulledtext.split()[25] +" "+ pulledtext.split()[26] +"\n")
                        timesheet += ("```")
                        embed = discord.Embed(title='**2x Schedule**', description=timesheet, color=self.orange)
                        await self.bot.say(embed=embed)
                    elif pulledlen >= 18 :
                        timesheet = ("```xl")
                        timesheet += ("\n")
                        timesheet += (pulledtext.split()[0] + " | " + pulledtext.split()[1] +" "+ pulledtext.split()[2] +"\n")
                        timesheet += (pulledtext.split()[3] + " | " + pulledtext.split()[4] +" "+ pulledtext.split()[5] +"\n")
                        timesheet += (pulledtext.split()[6] + " | " + pulledtext.split()[7] +" "+ pulledtext.split()[8] +"\n")
                        timesheet += ("```")
                        timesheet += ("\n")
                        timesheet += ("```xl")
                        timesheet += ("\n")
                        timesheet += (pulledtext.split()[9] + " | " + pulledtext.split()[10] +" "+ pulledtext.split()[11] +"\n")
                        timesheet += (pulledtext.split()[12] + " | " + pulledtext.split()[13] +" "+ pulledtext.split()[14] +"\n")
                        timesheet += (pulledtext.split()[15] + " | " + pulledtext.split()[16] +" "+ pulledtext.split()[17] +"\n")
                        timesheet += ("```")
                        embed = discord.Embed(title='**2x Schedule**', description=timesheet, color=self.orange)
                        await self.bot.say(embed=embed)
                    elif pulledlen >= 9 :
                        timesheet = ("```xl")
                        timesheet += ("\n")
                        timesheet += (pulledtext.split()[0] + " | " + pulledtext.split()[1] +" "+ pulledtext.split()[2] +"\n")
                        timesheet += (pulledtext.split()[3] + " | " + pulledtext.split()[4] +" "+ pulledtext.split()[5] +"\n")
                        timesheet += (pulledtext.split()[6] + " | " + pulledtext.split()[7] +" "+ pulledtext.split()[8] +"\n")
                        timesheet += ("```")
                        embed = discord.Embed(title='**2x Schedule**', description=timesheet, color=self.orange)
                        await self.bot.say(embed=embed)
                    else:
                        timesheet = "Nope"
                        embed = discord.Embed(title='**2x Schedule**', description=timesheet, color=self.orange)
                        await self.bot.say(embed=embed)
    
    @commands.command()
    async def check2x(self):
        """Displays known 2x dates and times"""
        
        #website = 'https://ijgfbhygk9.execute-api.us-west-2.amazonaws.com/prod/getEventTimes'
        #r = requests.get(website)
        #soup = BeautifulSoup(r.text, 'lxml')
        #for datapull in soup.find_all('body'):
        #    pulledtext = datapull.text
        #    embed = discord.Embed(title='**2x Schedule**', description=pulledtext, color=self.orange)
        #    await self.bot.say(embed=embed)
            
        website = 'https://ijgfbhygk9.execute-api.us-west-2.amazonaws.com/prod/getEventTimes'
        r = requests.get(website)
        soup = BeautifulSoup(r.text, 'lxml')
        for datapull in soup.find_all('body'):
            pulledtext = datapull.text
            pulledsplit = pulledtext.split()
            pulledlen = len(pulledsplit)
            if pulledlen > 28 :
                timesheet = "The dumbass mod put too many 2x times on the schedule."
                embed = discord.Embed(title='**2x Schedule**', description=timesheet, color=self.orange)
                await self.bot.say(embed=embed)
            elif pulledlen >= 27 :
                timesheet = (pulledtext.split()[0] + " | " + pulledtext.split()[1] +" "+ pulledtext.split()[2] +"\n")
                timesheet += (pulledtext.split()[3] + " | " + pulledtext.split()[4] +" "+ pulledtext.split()[5] +"\n")
                timesheet += (pulledtext.split()[6] + " | " + pulledtext.split()[7] +" "+ pulledtext.split()[8] +"\n\n")
                timesheet += (pulledtext.split()[9] + " | " + pulledtext.split()[10] +" "+ pulledtext.split()[11] +"\n")
                timesheet += (pulledtext.split()[12] + " | " + pulledtext.split()[13] +" "+ pulledtext.split()[14] +"\n")
                timesheet += (pulledtext.split()[15] + " | " + pulledtext.split()[16] +" "+ pulledtext.split()[17] +"\n\n")
                timesheet += (pulledtext.split()[18] + " | " + pulledtext.split()[19] +" "+ pulledtext.split()[20] +"\n")
                timesheet += (pulledtext.split()[21] + " | " + pulledtext.split()[22] +" "+ pulledtext.split()[23] +"\n")
                timesheet += (pulledtext.split()[24] + " | " + pulledtext.split()[25] +" "+ pulledtext.split()[26] )
                embed = discord.Embed(title='**2x Schedule**', description=timesheet, color=self.orange)
                await self.bot.say(embed=embed)
            elif pulledlen >= 18 :
                timesheet = (pulledtext.split()[0] + " | " + pulledtext.split()[1] +" "+ pulledtext.split()[2] +"\n")
                timesheet += (pulledtext.split()[3] + " | " + pulledtext.split()[4] +" "+ pulledtext.split()[5] +"\n")
                timesheet += (pulledtext.split()[6] + " | " + pulledtext.split()[7] +" "+ pulledtext.split()[8] +"\n\n")
                timesheet += (pulledtext.split()[9] + " | " + pulledtext.split()[10] +" "+ pulledtext.split()[11] +"\n")
                timesheet += (pulledtext.split()[12] + " | " + pulledtext.split()[13] +" "+ pulledtext.split()[14] +"\n")
                timesheet += (pulledtext.split()[15] + " | " + pulledtext.split()[16] +" "+ pulledtext.split()[17] )
                embed = discord.Embed(title='**2x Schedule**', description=timesheet, color=self.orange)
                await self.bot.say(embed=embed)
            elif pulledlen >= 9 :
                timesheet = (pulledtext.split()[0] + " | " + pulledtext.split()[1] +" "+ pulledtext.split()[2] +"\n")
                timesheet += (pulledtext.split()[3] + " | " + pulledtext.split()[4] +" "+ pulledtext.split()[5] +"\n")
                timesheet += (pulledtext.split()[6] + " | " + pulledtext.split()[7] +" "+ pulledtext.split()[8] )
                embed = discord.Embed(title='**2x Schedule**', description=timesheet, color=self.orange)
                await self.bot.say(embed=embed)
            else:
                timesheet = "Nope"
                embed = discord.Embed(title='**2x Schedule**', description=timesheet, color=self.orange)
                await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(twoX(bot))
