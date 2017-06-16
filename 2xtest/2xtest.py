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

        timedict = {}
        timedict['12:00AM'] = 0
        timedict['1:00AM'] = 1
        timedict['2:00AM'] = 2
        timedict['3:00AM'] = 3
        timedict['4:00AM'] = 4
        timedict['5:00AM'] = 5
        timedict['6:00AM'] = 6
        timedict['7:00AM'] = 7
        timedict['8:00AM'] = 8
        timedict['9:00AM'] = 9
        timedict['10:00AM'] = 10
        timedict['11:00AM'] = 11
        timedict['12:00PM'] = 12
        timedict['1:00PM'] = 13
        timedict['2:00PM'] = 14
        timedict['3:00PM'] = 15
        timedict['4:00PM'] = 16
        timedict['5:00PM'] = 17
        timedict['6:00PM'] = 18
        timedict['7:00PM'] = 19
        timedict['8:00PM'] = 20
        timedict['9:00PM'] = 21
        timedict['10:00PM'] = 22
        timedict['11:00PM'] = 23

        monthdict = {}
        monthdict['january'] = 1
        monthdict['february'] = 2
        monthdict['march'] = 3
        monthdict['april'] = 4
        monthdict['may'] = 5
        monthdict['june'] = 6
        monthdict['july'] = 7
        monthdict['august'] = 8
        monthdict['september'] = 9
        monthdict['october'] = 10
        monthdict['november'] = 11
        monthdict['december'] = 12

        add_hours_for_testing = 0

        # will need to be changed to -7 during daylight savings
        # or look into "pytz" module for more accurate pst/pdt calculation
        pst_timedifference = -8

        currentyear = datetime.utcnow().year
        currenttimepst = datetime.utcnow() + timedelta(hours=pst_timedifference) + timedelta(hours=add_hours_for_testing)

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
