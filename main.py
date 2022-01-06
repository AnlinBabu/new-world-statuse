import discord
from discord.ext import commands
import json
import pytz
from datetime import datetime
from tzlocal import get_localzone
from os import listdir

# Uses discord.py
# Docs at: https://discordpy.readthedocs.io/en/stable/

# Discord bot token
# Instructions to generate at: https://discordpy.readthedocs.io/en/stable/discord.html
token = ""
prefix = "!"

def print_log(message):
    print("%s | %s" % (datetime.now().astimezone(get_localzone()), message))

bot = commands.Bot(prefix)

# Load cogs
for file in listdir('cogs/'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')

@bot.event
async def on_connect():
    print_log("Logging in to discord")

@bot.event
async def on_ready():
    print_log("Logged in as {0.user}".format(bot))

@bot.event
async def on_resumed():
    print_log("Resumed")

@bot.event
async def shutdown(self):
    print_log("Closing connection to Discord...")

@bot.event
async def close():
    print_log("Closing on keyboard interrupt...")

@bot.event
async def on_disconnect():
    print_log("Bot disconnected.")

bot.run(token)