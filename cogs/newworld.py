import discord
from discord.ext import commands
import requests
import json
import pytz
from datetime import datetime
from tzlocal import get_localzone

# New World status API Key
# Request API Key at: https://newworldstatus.com/__automata/gtm/request.aspx
nwskey = ""

def print_log(message):
    print("%s | %s" % (datetime.now().astimezone(get_localzone()), message))

def get_status(world="delos"):
    world = world.lower().strip()
    url = requests.get("https://firstlight.newworldstatus.com/ext/v1/worlds/" + world, headers={"Accept":"application/json","Authorization":nwskey})
    text = url.text

    data = None

    try:
        data = json.loads(text)
    except:
        data['success'] = False

    world = world[0].upper() + world[1:]
    message = ''

    if (data['success'] and data['message']['status_enum'] == 'ACTIVE'):
        message += world + " is online\n"
        message += "```\n"
        message += "Online Players: %d/%d (%.2f%% full)\n" % (data['message']['players_current'], data['message']['players_maximum'], (data['message']['players_current'] / data['message']['players_maximum'] * 100))
        message += "Queue:          %d\n" % data['message']['queue_current']
        message += "Wait time:      %d minutes" % data['message']['queue_wait_time_minutes']
        message += "```\n"
        message += "More details: https://newworldstatus.com/worlds/" + world.lower()
    elif (data['success'] and not data['message']['status_enum'] == 'ACTIVE'):
        message += world + " is not online"
    elif not data['success']:
        message += data['message']
    else:
        message += "There was an error accessing the API\n"
        message += str(text)
    
    return(message)

class New_World(commands.Cog, name="New World"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['world','server'], name="status")
    @commands.guild_only()
    async def status(self, ctx, *, world="delos"):
        """Gets the status of a world.
        If no world is provided, it gets the status of delos.
        Other information retrieved:
            Online players
            Maximum players
            Queue length
            Queue wait time"""
        print_log("%s used !status in '%s' '#%s'" % (ctx.author, ctx.guild.name, ctx.channel.name))
        try:
            message = await ctx.send("Querying")
            await ctx.send(get_status(world))
            await message.delete()
        except:
            print_log("error")

# Required at the end of every cog to add it to the bot
def setup(bot):
    bot.add_cog(New_World(bot))