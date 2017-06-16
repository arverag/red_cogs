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

        linkPart = []
        mainPage = ("https://e8tdwagy36.execute-api.us-west-2.amazonaws.com/prod/getTimeUntilNextEvent")
        try:
            try:
                htmltext = urllib.request.urlopen(mainPage).read()
                regex = '<pre>(.*?)</pre>'
                matches = re.findall(re.compile(regex), htmltext)
                match = "none"

                endTimes = []

                for i in range(0, len(matches)):
                    endTimes.append(matches)

                if match == "none":
                    match = []
                    raise Exception()
            except:
                await self.bot.say("The next 2x event has not been announced yet in a supported format.")

            eventPage = "https://e8tdwagy36.execute-api.us-west-2.amazonaws.com/prod/getTimeUntilNextEvent"
            try:
                htmltext = urllib.request.urlopen(eventPage).read()
                regex = '<pre>(.*?)</pre>'
                htmltext = re.findall(re.compile(regex), htmltext)

                regex = '<pre>(.*?)</pre>'
                matches = re.findall(re.compile(regex), htmltext)

                stringtosay = ".."

                if len(endTimes) == 0:
                    stringtosay = stringtosay + "\r\nThe next 2x event has not been announced yet."

                except:
                    nextEndtime = endTimes[0]
                    if len(startTimes) == 0 or startTimes[0] - nextEndtime > timedelta(seconds=0):
                        timeSpan = nextEndtime.replace(microsecond=0) - currenttimepst.replace(microsecond=0)
                        stringtosay = stringtosay + " (" + endTimes + ")"

                await self.bot.say(stringtosay)

            except Exception as e:
                await self.bot.say("Something broke! Try contacting @boardwalk hotel to get it fixed")
                traceback.print_exc()
        except:
            e = 5

def setup(bot):
    bot.add_cog(twoXcog(bot))
