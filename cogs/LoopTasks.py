from discord.ext import commands, tasks
from cogs.SelectStatistics import SelectStatistic
from cogs.UtilityFunctions import EditView,FileOperations
from cogs.Events import Events
from discord import app_commands
import discord
import os
import json
import datetime
import pytz


timezone = pytz.timezone(FileOperations.select_server_timezone())
time = datetime.time(hour=23, minute=55,tzinfo=timezone)

class LoopTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_id = FileOperations.select_guild_id()

    #at 23.55 dumps count of messages to json file
    @tasks.loop(time=time)
    async def messages_count_json_export(self):
        try:
            json_data = FileOperations.read_json("daily_info.json")
            message_count = await SelectStatistic.select_message_count(self.bot,self.guild_id)
            json_data['messages_count'] = message_count
            FileOperations.write_json("daily_info.json",json_data)
        except Exception as e:
            print(e)


    #TO DO export users info to json
    @tasks.loop(seconds=10)
    async def members_info_json_export(self):
        try:
             
            json_data = FileOperations.read_json("members_info.json")
            members_info = await SelectStatistic.select_members_info(self.bot, self.guild_id)
            
            #if not json, create it
            if not json_data:
                json_data = {}
            
            #loop every active member
            for member_id, member_data in members_info.items():
                
                #if member in json, add time else create member
                if json_data.get(str(member_id)) != None:    
                    json_data[str(member_id)]['time'] += 10
                else:
                    json_data[member_id] = {'name': member_data['name'], 'time': 10}

            FileOperations.write_json("members_info.json", json_data)

        except Exception as e:
            print(e)


    #save json with number of active members
    @tasks.loop(minutes=1)
    async def member_count_json(self):
        try:
            print("START member_count_json")
            json_data = FileOperations.read_json("daily_info.json")
            
            json_data['members_count'] = await SelectStatistic.select_members_count(self.bot,self.guild_id)
            FileOperations.write_json("daily_info.json",json_data)
            print("STOP member_count_json")
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_ready(self):
        self.member_count_json.start()
        self.messages_count_json_export.start()
        self.members_info_json_export.start()
        self.test.start()


async def setup(bot):
    await bot.add_cog(LoopTasks(bot))