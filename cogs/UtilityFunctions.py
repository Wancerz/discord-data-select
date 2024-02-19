import discord
from discord.ext import commands, tasks
import json
from datetime import datetime, timedelta
from cogs.SelectStatistics import SelectStatistic
#server id 
#218510314835148802

class EditView(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    #Parse list with active members and create string with informations about active members
    @staticmethod
    async def parser_members_info(bot,guild_id):
        
        members_info =  await SelectStatistic.select_members_info(bot,guild_id)
              
        if not members_info:
            return False
        
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
        return result


    # @commands.Cog.listener()
    # async def on_ready(self):
        



async def setup(bot):
    await bot.add_cog(EditView(bot))