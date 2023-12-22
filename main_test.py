import discord
from discord.ext import commands, tasks
import asyncio

from discord.message import Message

intents = discord.Intents.all()

# class Tasks():
#     def __init__(self,bot) -> None:
#         self.bot = bot
#         pass




# class BackgroundTasks():
#     def __init__(self, bot):
#         self.bot = bot
#         self.select_users_at_channel.start()

#     async def select_channels(self):
#         SERVER_ID = 218510314835148802
        
#         guild = self.bot.get_guild(SERVER_ID)



    

#     @tasks.loop(seconds=30)
#     async def select_users_at_channel(self):
#         # Your background task code goes here
        




#         for guild in self.bot.guilds:
#             print("Nazwa serwera",guild.name)
            
#             print("ID serwera",guild.id)
            

#             for channel in guild.voice_channels:
#                 print("nazwa kanalu glosowego",channel.name," ID kanalu glosowego ", channel.id)


# #######################################################################
#             channel_names = []
#             for channel in guild.text_channels:
#                 #print("nazwa kanału:", channel.name)
                
#                 channel_names.append(channel.name)
#                 #channel.send("nazwa kanału:", channel.name)
#                 #print(channel.id)
# #######################################################################


#         channel_id = 1031514292647890944
#         channel = self.bot.get_channel(channel_id)
        
#         print("channel_name",channel.name)



#         channel_users = []
#         if channel:
#             for member in channel.members:
#                 print(member.name) 
#                 channel_users.append(member.name)




#             text_channel_id = 796794980810620948
#             text_channel = self.bot.get_channel(text_channel_id)
#             count = len(channel_users)
#             print(count)
#             channel_users_len = len(channel_users)
#             result = "liczba uzytkowników na kanale: " + str(channel_users_len) + " lista: " + str(channel_users)
#             #if text_channel:
                

#                 #await text_channel.send(result)

#         print("Background task executed!")



class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.add_command(self.test)
        
        print("111")

    @self.command(name='test')
    async def test(self,ctx):
        print("AAA")
        await ctx.send("AAA")




    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        # self.background_tasks = BackgroundTasks(self)
        print("222")
    # Your other commands and event handlers go here

async def main():
    bot = MyBot(command_prefix="!")
    await bot.start('MTE4NzEwOTMxMDE3MDM5ODg1Mg.GYaZVy.w_fglKspD2EDlwaTR4h6t8EymzPPVrNbPBpNGs')

if __name__ == "__main__":
    asyncio.run(main())