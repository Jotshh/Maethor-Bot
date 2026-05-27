import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

import os

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.palavroes_file = "data/palavroes.txt"

    def get_palavroes(self):
        try:
            with open(self.palavroes_file, "r", encoding="utf-8") as f:
                return [linha.strip().lower() for linha in f if linha.strip()]
        except FileNotFoundError:
            return []

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return

        content_lower = message.content.lower()
        palavroes = self.get_palavroes()

        if any(palavrao in content_lower for palavrao in palavroes):
            import random
            from bot.utils.points_db import remove_points
            
            punicoes = [5, 15, 50, 500]
            pesos = [70, 15, 10, 5]
            punicao_escolhida = random.choices(punicoes, weights=pesos, k=1)[0]
            
            pontos = remove_points(message.author.id, punicao_escolhida)
            await message.reply(f"Meeeee, cadê a classe? {message.author.mention} perdeu {punicao_escolhida} anos de amizade! (Total: {pontos} anos)")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        cargo_id = 833389853176627230
        
        if not isinstance(cargo_id, str):
            cargo_burro = member.guild.get_role(cargo_id)
            if cargo_burro:
                await member.add_roles(cargo_burro)

    @commands.command(name="clear", aliases=["limpar"])
    @commands.has_role(833389853176627230) 
    async def clear(self, ctx, amount: int):
        if amount > 100:
            return await ctx.send("❌ Você só pode apagar até 100 mensagens de uma vez!")
        elif amount <= 0:
            return await ctx.send("❌ Informe um número válido maior que 0!")

        deleted = await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f"✅ {len(deleted) - 1} mensagens apagadas por {ctx.author.mention}!")
        
        import asyncio
        await asyncio.sleep(5)
        await msg.delete()

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("❌ Você não tem permissão para usar este comando.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ Uso correto: `.clear <numero>`")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ Por favor, informe um número válido.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
