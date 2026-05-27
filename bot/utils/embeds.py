import discord
from datetime import datetime, timezone, timedelta

def create_embed(title=None, description=None, color=discord.Color.blue()):
    tz_amazonas = timezone(timedelta(hours=-4))
    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
        timestamp=datetime.now(tz_amazonas)
    )
    embed.set_footer(text="Desenvolvido por Maethor")
    return embed

def success_embed(**kwargs):
    return create_embed(color=discord.Color.green(), **kwargs)

def error_embed(**kwargs):
    return create_embed(color=discord.Color.red(), **kwargs)

def warning_embed(**kwargs):
    return create_embed(color=discord.Color.orange(), **kwargs)

