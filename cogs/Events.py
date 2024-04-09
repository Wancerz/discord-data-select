from discord.ext import commands, tasks
from cogs.SelectStatistics import SelectStatistic
from cogs.UtilityFunctions import EditView,FileOperations
from discord import app_commands
import discord
import os
from datetime import datetime, timedelta
import pytz


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_id = FileOperations.select_guild_id()
        self.member_activity = {}
        self.timezone = pytz.timezone(FileOperations.select_server_timezone())
        self.member_time = []


    async def select_member_activity(self):
        # print(self.member_activity)
        return self.member_activity
        
    # @commands.Cog.listener()
    # async def on_voice_state_update(self, member, before, after):
    #     try:
    #         print(self.member_activity)
    #         if before.channel != after.channel:
    #             if after.channel is not None:  # Member joined a voice channel
    #                 if member.id not in self.member_activity:
    #                     self.member_activity[member.id] = {'total_time': timedelta(), 'start_time': datetime.now(self.timezone)}
    #                 else:
    #                     self.member_activity[member.id]['start_time'] = datetime.now(self.timezone)
    #             if before.channel is not None:  # Member left a voice channel
    #                 if member.id in self.member_activity:
    #                     duration = datetime.now(self.timezone) - self.member_activity[member.id]['start_time']
    #                     self.member_activity[member.id]['total_time'] += duration  # Update total time
    #                     print(f"{member.display_name} was active for {duration} (Total: {self.member_activity[member.id]['total_time']})")
    #                     FileOperations.write_json("members_duration.json",self.member_activity)
    #     except Exception as e:
    #         print(f"An error occurred: {e}")


    # @tasks.loop(minutes=1)  # Run this task every minute
    # async def save_data(self):
    #     current_time = datetime.now(self.warsaw_timezone)
    #     if current_time.hour == 23 and current_time.minute == 58:
    #         FileOperations.write_json("members_time.json",self.member_activity)


async def setup(bot):
    bot.duration_data = {}
    await bot.add_cog(Events(bot))