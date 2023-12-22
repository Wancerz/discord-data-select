
import discord
from discord.ext import commands

class SelectStatiscs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        #self._last_member = None

    @commands.command(name='test')
    async def test(self,ctx):
        print("AAA")
        await ctx.send("AAA")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong")

    @commands.Cog.listener()
    async def on_ready(self):
        #print(f'Logged in as {user.name} ({user.id})')
        # self.background_tasks = BackgroundTasks(self)
        print("logged")



async def setup(bot):
    await bot.add_cog(SelectStatiscs(bot))