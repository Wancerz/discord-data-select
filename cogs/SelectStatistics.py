
import discord
from discord.ext import commands, tasks
import json
from datetime import datetime, timedelta

#server id 
#218510314835148802

class SelectStatistic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_id = 218510314835148802 

    #returns count of active users at server 
    def select_members_count(self):
        guild_id = self.guild_id
        server_instance = self.bot.get_guild(guild_id)

        if server_instance:
            #Get channels and append to "self.active_members" count of active members at channels 
            channels = server_instance.channels
            active_members = 0
            for channel in channels:
                if str(channel.type) == "voice":
                    active_members = active_members + len(channel.members)

        return active_members

    #returns sum of messages of today 
    async def select_message_count(self):
        guild_id = self.guild_id
        server_instance = self.bot.get_guild(guild_id)
        message_counter = 0
        today = today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=1)
               
        if server_instance:
            channels = server_instance.text_channels
            for channel in channels:

                async for message in channel.history(limit=200, after=today):
                    message_counter += 1
        
        return message_counter
    
    #returns ids of active members
    async def select_members_id(self):
        
        guild_id = self.guild_id
        server_instance = self.bot.get_guild(guild_id)
        members_id = []

        if server_instance:
            channels = server_instance.voice_channels
            for channel in channels:
                #check channel is not empty
                if channel.members:
                    for member in channel.members:
                        members_id.append(member.id)
                        # print(member.id)
        
        #delete duplicated ids
        unique_members_id = set(members_id)

        return unique_members_id


    #returns info about active members
    async def select_members_info(self):   
        guild_id = self.guild_id
        server_instance = self.bot.get_guild(guild_id)
        members_info = {}

        if server_instance:
            members_id = await self.select_members_id()

            for member_id in members_id:
                try:
                    member = server_instance.get_member(member_id) 

                    members_info[member_id] = {'name':member.name,'display_name':member.display_name,'created_at':member.created_at,'roles':member.roles,'status':member.status,'activity':member.activity}
                    # print(members_info,"\n\n")                        
                except:
                    continue
            # print(members_info)
        return members_info







    #loop saves collected server data to a json file at server
    @tasks.loop(seconds=60)
    async def JsonExport(self):
        print("Getting members count")
        json_data = {}
        json_data['members_count'] = self.SelectMembersCount()
        print("Members count obtained:", json_data['members_count'])

        json_data = json.dumps(json_data, indent=2)

        with open('output.json', 'w') as file:
            file.write(json_data)

        print("JSON file written")



    @commands.command(name='test')
    async def test(self,ctx):
        print("AAA")
        #server_id = ctx.guild.id
        guild_id = 218510314835148802
        server_instance = self.bot.get_guild(guild_id)
        # print(server_instance)
        if server_instance:

            #Get channels and append to "self.active_members" count of active members at channels 
            channels = server_instance.channels
            self.active_members = 0

            for channel in channels:
                if str(channel.type) == "voice":
                    self.active_members = self.active_members + len(channel.members)

          
        # print(self.voice_channles_id)
        print(self.active_members)


        # print(guild_id)
        await ctx.send(f"AAA {guild_id}")



    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong")

    @commands.Cog.listener()
    async def on_ready(self):
        print("logged")
        # self.JsonExport.start()


async def setup(bot):
    await bot.add_cog(SelectStatistic(bot))