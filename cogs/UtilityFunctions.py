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
        
        embed = discord.Embed(
            colour=discord.Colour.dark_blue(),
            description="Basic informations about active members",
            title="Members Info",

        )
        # embed.set_footer(text="NagiosXI-analysis")
        embed.set_author(name="NagiosXI-analysis")
        members_info =  await SelectStatistic.select_members_info(bot,guild_id)
              
        if not members_info:
            return False
        
        for member_id, member_data in members_info.items():
            member_name = member_data['name']
            member_display_name = member_data['display_name']
            member_created_at = member_data['created_at']
            # member_roles = member_data['roles']
            member_status = member_data['status']
            member_activity = member_data['activity']

            embed.add_field(
                name=f"**{member_name}**",
                inline=False,
                value =(f"**Nazwa uzytkownika**: {member_name} \n"
                        f"**Wyswietlana nazwa**: {member_display_name} \n"
                        f"**Data utworzenia konta**: {member_created_at} \n"
                        f"**Status**: {member_status} \n"
                        f"**Aktywnosci**: {member_activity}"))
            
        return embed


    # @commands.Cog.listener()
    # async def on_ready(self):
        



async def setup(bot):
    await bot.add_cog(EditView(bot))