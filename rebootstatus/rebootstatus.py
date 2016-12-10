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
