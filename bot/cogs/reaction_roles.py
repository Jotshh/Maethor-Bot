import discord
from discord.ext import commands
from discord.ui import View, Button

class RoleButton(Button):
    def __init__(self, role: discord.Role, emoji: str):
        super().__init__(
            label=role.name,
            emoji=emoji,
            style=discord.ButtonStyle.primary,
            custom_id=f"role_{role.id}"
        )
        self.role = role
    
    async def callback(self, interaction: discord.Interaction):
        member = interaction.user
        
        if self.role in member.roles:
            await member.remove_roles(self.role)
            await interaction.response.send_message(
                f"❌ Cargo **{self.role.name}** removido!",
                ephemeral=True
            )
        else:
            await member.add_roles(self.role)
            await interaction.response.send_message(
                f"✅ Cargo **{self.role.name}** adicionado!",
                ephemeral=True
            )
            
        import asyncio
        await asyncio.sleep(5)
        try:
            await interaction.delete_original_response()
        except discord.HTTPException:
            pass

class ButtonRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="cargos", aliases=["roles"])
    @commands.has_permissions(administrator=True)
    async def button_roles(self, ctx: commands.Context):
        
        view = View(timeout=None)
        
        roles_config = [
            ("🎮", 1419092863857197188), 
            ("🔫", 1429840292487630911),  
        ]
        
        for emoji, role_id in roles_config:
            if isinstance(role_id, str):
                continue
                
            role = ctx.guild.get_role(role_id)
            if role:
                view.add_item(RoleButton(role, emoji))
        
        embed = discord.Embed(
            title="🎮 Escolha seus jogos!",
            description="Clique nos botões abaixo para receber ou remover a tag do jogo que você joga.",
            color=discord.Color.red()
        )
        
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(ButtonRoles(bot))