from discord.ext import commands
from cogs.SelectStatistics import SelectStatistic
from cogs.UtilityFunctions import EditView
from discord import app_commands
import discord



class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_id = 218510314835148802 

    #return count of messages
    @commands.command(name='message_count')
    async def message_count(self,ctx):  
        message_count = await SelectStatistic.select_message_count(self.bot,self.guild_id)

        await ctx.send(f"Liczba dzisiejszych wiadomości: {message_count}")

    #return count of members on voice channels
    @commands.command(name='active_members_count')
    async def active_members_count(self,ctx):

        active_members = await SelectStatistic.select_members_count(self.bot,self.guild_id)
        await ctx.send(f"liczba aktywnych uzytkownikow: {active_members}")



    #return array with ID of active members
    @commands.command(name='active_members_id')
    async def active_members_id(self,ctx):

        active_members_id = await SelectStatistic.select_members_id(self.bot,self.guild_id)
        await ctx.send(f"ID aktywnych uzytkownikow: {active_members_id}")



    #return info about active members
    @commands.command(name="active_members_info")
    async def active_members_info(self,ctx):

        result = await EditView.parser_members_info(self.bot,self.guild_id)
        if not result:
            await ctx.send("No active members found.")
        else:
            await ctx.send(embed=result)
            # await ctx.send(f"Informacje o aktywnych uzytkownikach:\n {result}")



    @commands.command(name="sync")
    async def sync(self,ctx):
        synced = await self.bot.tree.sync()
        await ctx.send(f"Synced {len(synced)} command(s).")





async def setup(bot):
    await bot.add_cog(Commands(bot))

