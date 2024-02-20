from discord.ext import commands
from cogs.SelectStatistics import SelectStatistic
from cogs.UtilityFunctions import EditView,FileOperations
from discord import app_commands
import discord
import os


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_id = FileOperations.select_guild_id()

    #return count of messages via slash command
    @app_commands.command(name='message_count', description="return the number of messages from today")
    async def message_count_slash(self, interaction: discord.Interaction):  
        try:
            #defer timeout of interaction
            await interaction.response.defer()
            # await interaction.response.send_message(f"oczekuje na dane")
            #select messages count
            message_count = await SelectStatistic.select_message_count(self.bot,self.guild_id)
            # await interaction.edit_original_response(content=f"Liczba dzisiejszych wiadomości: {message_count}")

            #if awaited method returns messages count send it via defered interaction
            await interaction.followup.send(f"Liczba dzisiejszych wiadomości: {message_count}")
        except Exception as e :
            print(e)
            await interaction.response.send_message(e)

    #return count of members on voice channels via slash command
    @app_commands.command(name='active_members_count', description="return count of active members")
    async def active_members_count_slash(self,interaction: discord.Interaction):
        try:
            await interaction.response.defer()
            active_members = await SelectStatistic.select_members_count(self.bot,self.guild_id)
            await interaction.followup.send(f"liczba aktywnych uzytkownikow: {active_members}")
        except Exception as e:
            print(e)
            await interaction.response.send_message(e)
        
    #return array with ID of active members via slash command
    @app_commands.command(name='active_members_id', description="return IDs of active members")
    async def active_members_id(self,interaction: discord.Interaction):
        try:
            await interaction.response.defer()
            active_members_id = await SelectStatistic.select_members_id(self.bot,self.guild_id)
            await interaction.followup.send(f"ID aktywnych użytkowników: {active_members_id}")
        except Exception as e:
            print(e)
            await interaction.response.send_message(e)
        
    #return info about active members via slash command
    @app_commands.command(name="active_members_info",description="return basic info about active members")
    async def active_members_info(self,interaction: discord.Interaction):
        try:
            await interaction.response.defer()
            result = await EditView.parser_members_info(self.bot,self.guild_id)
            if not result:
                await interaction.followup.send(embed=f"no active members")
            else:
                await interaction.followup.send(embed=result)
        except Exception as e:
            print(e)
            

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(SlashCommands(bot))