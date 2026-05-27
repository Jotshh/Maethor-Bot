import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
import sys
from datetime import datetime, timezone, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=".",  
    intents=intents
)

async def load_cogs():
    for filename in os.listdir('./bot/cogs'):
        if filename.endswith('.py') and not filename.startswith('__'):
            try:
                await bot.load_extension(f'bot.cogs.{filename[:-3]}')
                print(f"✅ Cog carregado: {filename}")
            except Exception as e:
                print(f"❌ Erro ao carregar {filename}: {e}")

bot.setup_hook = load_cogs

@bot.event
async def on_ready():
    print(f"✅ Bot ligado como {bot.user}")
    print(f"ID: {bot.user.id}")

    await bot.change_presence(
        activity=discord.Activity(
        type=discord.ActivityType.playing,
        name="League of Legends ou em chamada..."))

@bot.command()
async def ola(ctx):
    await ctx.send(f"Olá, {ctx.author.mention}!")

@bot.command()
async def lol(ctx:commands.Context):
    cargo_lol = ctx.guild.get_role(1419092863857197188)  
    tz_amazonas = timezone(timedelta(hours=-4))

    embedLol = discord.Embed(   
        title=":video_game: E o lolzinho cade?! ",
        description=f"{cargo_lol.mention if cargo_lol else '@cargo_desconhecido'} Alguém online?",
        color=0xF1C40F,
        timestamp=datetime.now(tz_amazonas)
    )
    imagem = discord.File("assets/league-sinal.png", "lol.png")
    embedLol.set_image(url="attachment://lol.png")

    membros_count = str(len(cargo_lol.members)) if cargo_lol else "0"
    embedLol.add_field(
        name=":bar_chart: Membros no cargo",
        value=membros_count,
        inline=True
    )
    
    embedLol.set_footer(text=f"Solicitado por {ctx.author.name}", 
                        icon_url=ctx.author.avatar)
    usuario_id = 459412182619127809
    await ctx.send(f"Chamando {cargo_lol.mention if cargo_lol else '@cargo_desconhecido'} e <@{usuario_id}>!")
    await ctx.send(embed=embedLol, file=imagem)

if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("❌ ERRO: Token não encontrado no arquivo .env")
    else:
        bot.run(token)