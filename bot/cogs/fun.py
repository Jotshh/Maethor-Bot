import discord
from discord.ext import commands
from bot.utils.embeds import success_embed, error_embed

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        import random
        if message.author.bot:
            return
            
        if message.author.id == 866335765658337301 and random.random() <= 0.25:
            respostas_chatas = [
                "Lá vem ele com as perguntinhas do chat...",
                "Ah não, dá um castiguinho nele...",
                "É né, biel?"
            ]
            await message.reply(random.choice(respostas_chatas))
            return 

        if self.bot.user in message.mentions:              
            frases = [
                "Fala mordedor...",
                "Calma aí... Dá o mouse, Ni...",
                "É o que eu sempre digo... Não houve ditadura e sim regime autoritário militar...",
                "Meeeeeeeeeeeee.",
                "Como é mesmo aquela música? A noite da Arábia... e o dia também...",
                "Eu já disse biel, sou main, não mono...",
                "Aiai, é muita narrativa...",
                "Ele não conseguem farmar mais aura que eu...",
                "DEIXA O BO AQUI 😠."
            ]
            resposta = random.choice(frases)
            await message.reply(resposta)
    
    @commands.command(name='roll')
    async def roll(self, ctx, dice: str = '1d6'):
        try:
            number, sides = map(int, dice.split('d'))
            if number > 100 or sides > 100:
                raise ValueError
            
            import random
            rolls = [random.randint(1, sides) for _ in range(number)]
            total = sum(rolls)
            
            embed = success_embed(
                title="🎲 Rolagem de Dados",
                description=f"Resultado: **{total}**"

            )
            await ctx.send(f"O usuário, {ctx.author.mention}, rolou o seguinte dado:")
            await ctx.send(embed=embed)
            
        except:
            embed = error_embed(
                title="Erro",
                description="Formato inválido! Use: .roll [NdN]"
            )
            await ctx.send(embed=embed)

    @commands.command(name='boneco', aliases=['pick', 'champ'])
    async def boneco(self, ctx, grupo: str = 'todos'):
        import random
        import json
        
        caminho_arquivo = "data/bonecos.json"
        
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
        except FileNotFoundError:
            await ctx.reply("❌ Arquivo de bonecos não encontrado!")
            return
            
        bonecos = dados.get(grupo.lower())
        
        if not bonecos:
            grupos_disponiveis = ", ".join(dados.keys())
            await ctx.reply(f"❌ Grupo não encontrado! Grupos disponíveis: **{grupos_disponiveis}**")
            return
            
        escolhido = random.choice(bonecos)
        await ctx.reply(f"🎲 Vai jogar de: **{escolhido}**!")

async def setup(bot):
    await bot.add_cog(Fun(bot))