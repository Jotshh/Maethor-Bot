import discord
from discord.ext import commands
import os

class MeuBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        
        super().__init__(
            command_prefix=".",
            intents=intents,
            case_insensitive=True
        )
    
    async def setup_hook(self):
        await self.load_extension('bot.cogs.comandos')
        print("✅ Cogs carregados!")
    
    async def on_ready(self):
        print(f"✅ {self.user} está online!")
        await self.change_presence(
            activity=discord.Game(name=".ajuda")
        )