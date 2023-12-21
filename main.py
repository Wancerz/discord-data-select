import discord
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.all()


class BackgroundTasks():
    def __init__(self, bot):
        self.bot = bot
        self.select_users_at_channel.start()

    @tasks.loop(seconds=30)
    async def select_users_at_channel(self):
        # Your background task code goes here



        for guild in self.bot.guilds:
            print("Nazwa serwera",guild.name)
            
            print("ID serwera",guild.id)
            
            for  voice in guild.voice_channels:
                print(voice.name)


            channel_names = []
            for channel in guild.text_channels:
                #print("nazwa kanału:", channel.name)
                
                channel_names.append(channel.name)
                #channel.send("nazwa kanału:", channel.name)
                print("id kanału",channel.id)

        channel_id = 796794980810620948
        channel = self.bot.get_channel(channel_id)

        print(channel_names)

        #if channel: 
            #await channel.send(channel_names) 
        #await channel.send(channel_names)

            #await channel.send("test")
        print("Background task executed!")



class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix, intents=intents)
        

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        self.background_tasks = BackgroundTasks(self)
    # Your other commands and event handlers go here

async def main():
    bot = MyBot(command_prefix="!")
    await bot.start('')

if __name__ == "__main__":
    asyncio.run(main())