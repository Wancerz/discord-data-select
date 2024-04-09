import discord
from discord.ext import commands, tasks
import os
import asyncio
from cogs.UtilityFunctions import FileOperations

intents = discord.Intents.all()
intents.message_content = True
# TOKEN = os.environ.get('TOKEN')
TOKEN = FileOperations.select_server_token()

print(TOKEN)


bot = commands.Bot(command_prefix='!', intents=intents)

async def load():
    for filename in os.listdir('./cogs'):
        print(filename)
        if filename.endswith(".py"):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())

