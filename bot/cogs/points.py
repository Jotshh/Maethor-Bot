from ctypes.util import test
import discord
from discord.ext import commands, tasks
from bot.utils.points_db import add_points, get_points

class Points(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_voice.start()

    def cog_unload(self):
        self.check_voice.cancel()

    @tasks.loop(minutes=30.0)
    async def check_voice(self):
        for guild in self.bot.guilds:
            for vc in guild.voice_channels:
                for member in vc.members:                    
                    if not member.bot:
                        if not member.voice.afk and not member.voice.self_deaf and not member.voice.deaf:
                            add_points(member.id, 15)

    @check_voice.before_loop
    async def before_check_voice(self):
        await self.bot.wait_until_ready()

    @commands.command(name="amizade", aliases=["pontos", "anos"])
    async def amizade(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        pontos = get_points(member.id)
        
        embed = discord.Embed(
            title="🔨 Anos de Amizade com Maethor",
            description=f"{member.mention} tem **{pontos}** anos de amizade com Maethor!",
            color=0x040287
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        
        if member.id == 342001359953985538:
            embed.set_footer(text="Ele é o Pedro né...")
        else:
            embed.set_footer(text="Mas se fosse o Pedro...")
            
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Points(bot))
