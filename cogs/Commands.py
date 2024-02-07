from discord.ext import commands
from cogs.SelectStatistics import SelectStatistic



class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    #return count of messages
    @commands.command(name='message_count')
    async def ReturnMessageCount(self,ctx):
        print("START")
        message_count = await self.select_statistic.SelectMessageCount()

        await ctx.send(f"Liczba dzisiejszych wiadomości: {message_count}")

    #return count of members on voice channels
    @commands.command(name='active_members_count')
    async def active_members_count(self,ctx):
        active_members = self.select_statistic.SelectMembersCount()

        await ctx.send(f"liczba aktywnych uzytkownikow: {active_members}")

    @commands.command(name='active_members_id')
    async def active_members_id(self,ctx):
        active_members_id = await self.select_statistic.SelectMemebersID()
        await ctx.send(f"ID aktywnych uzytkownikow: {active_members_id}")

    @commands.Cog.listener()
    async def on_ready(self):
        self.select_statistic = SelectStatistic(self.bot)

async def setup(bot):
    await bot.add_cog(Commands(bot))