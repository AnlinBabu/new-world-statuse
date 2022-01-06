from discord.ext import commands
from time import sleep


class Debug(commands.Cog, name="Debug"):

    def __init__(self, bot):
        self.bot = bot
    
    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def Cog_Load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            message = await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            message = await ctx.send('**`SUCCESS`**')

        sleep(1)
        await message.delete()
        await ctx.message.delete()

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def Cog_Unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            message = await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            message = await ctx.send('**`SUCCESS`**')

        sleep(1)
        await message.delete()
        await ctx.message.delete()

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def Cog_Reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            message = await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            message = await ctx.send('**`SUCCESS`**')
        
        sleep(1)
        await message.delete()
        await ctx.message.delete()

    @commands.command(name='delmessage', hidden=True)
    @commands.is_owner()
    async def Cog_DelMessage(self, ctx, *, id: int):
        """Delete a message from the bot
        Can also delete other messages if the bot has permission but is limited to the last 100 messages"""
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=100):
            if message.id == id:
                await message.delete()
        message = await ctx.send('**`SUCCESS`**')
        sleep(1)
        await message.delete()


def setup(bot):
    bot.add_cog(Debug(bot))