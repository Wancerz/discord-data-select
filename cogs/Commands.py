from discord.ext import commands
from cogs.SelectStatistics import SelectStatistic



class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    #return count of messages
    @commands.command(name='message_count')
    async def message_count(self,ctx):
        print("START")
        message_count = await self.select_statistic.select_message_count()

        await ctx.send(f"Liczba dzisiejszych wiadomości: {message_count}")

    #return count of members on voice channels
    @commands.command(name='active_members_count')
    async def active_members_count(self,ctx):
        active_members = self.select_statistic.select_members_count()

        await ctx.send(f"liczba aktywnych uzytkownikow: {active_members}")

    #return array with ID of active members
    @commands.command(name='active_members_id')
    async def active_members_id(self,ctx):
        active_members_id = await self.select_statistic.select_members_id()
        await ctx.send(f"ID aktywnych uzytkownikow: {active_members_id}")

    #return info about active members
    @commands.command(name="active_members_info")
    async def active_members_info(self,ctx):
        members_info = await self.select_statistic.select_members_info()

        if not members_info:
            await ctx.send("No active members found.")
            return

        result = "####################\n"
        for member_id, member_data in members_info.items():
            member_name = member_data['name']
            member_display_name = member_data['display_name']
            member_created_at = member_data['created_at']
            # member_roles = member_data['roles']
            member_status = member_data['status']
            member_activity = member_data['activity']

            result += f"Nazwa uzytkownika: {member_name} \nWyswietlana nazwa: {member_display_name} \nData utworzenia konta: {member_created_at} \nStatus: {member_status} \nAktywnosci: {member_activity}"
            result += "\n###################\n"
        print(result)
        
        # print(members_info)
        await ctx.send(f"Informacje o aktywnych uzytkownikach:\n {result}")

    

    @commands.Cog.listener()
    async def on_ready(self):
        self.select_statistic = SelectStatistic(self.bot)

async def setup(bot):
    await bot.add_cog(Commands(bot))