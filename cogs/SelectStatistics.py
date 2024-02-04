
import discord
from discord.ext import commands, tasks
import json
#server id 
#218510314835148802

class SelectStatiscs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 


    #returns count of active users at server 
    def SelectMembersCount(self):
        print("AAA")
        
        guild_id = 218510314835148802
        server_instance = self.bot.get_guild(guild_id)

        if server_instance:
            #Get channels and append to "self.active_members" count of active members at channels 
            channels = server_instance.channels
            active_members = 0
            for channel in channels:
                if str(channel.type) == "voice":
                    active_members = active_members + len(channel.members)

        print(active_members)
        return active_members

    @commands.command(name='active_members')
    async def active_members(self,ctx):
        active_members = self.SelectMembersCount()


        await ctx.send(f"liczba aktywnych uzytkownikow: {active_members}")

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




    @commands.command(name='test1')
    async def test1(self,ctx):


        await ctx.send("AAA")




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



            # for channel in channels:
            #     print(f"Channel Name: {channel.name}, Channel ID: {channel.id}, Channel Type: {channel.type}")
            
        # print(self.voice_channles_id)
        print(self.active_members)


        # print(guild_id)
        await ctx.send(f"AAA {guild_id}")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong")

    @commands.Cog.listener()
    async def on_ready(self):
        #print(f'Logged in as {user.name} ({user.id})')
        # self.background_tasks = BackgroundTasks(self)
        print("logged")
        self.JsonExport.start()






async def setup(bot):
    await bot.add_cog(SelectStatiscs(bot))