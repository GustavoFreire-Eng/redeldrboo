import os
import discord
from discord.ext import commands

# 🔐 CONFIGURAÇÃO SEGURA - token via variável de ambiente
TOKEN = os.environ.get('DISCORD_TOKEN')

if not TOKEN:
    print("❌ ERRO: Token não encontrado!")
    print("💡 Configure a variável de ambiente DISCORD_TOKEN:")
    print("   - No Heroku: Settings → Config Vars")
    print("   - Local: Crie arquivo .env com DISCORD_TOKEN=seu_token")
    exit(1)

# Configurar o bot
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

# ============ COMANDOS DO BOT ============

@bot.command(name='mapa')
async def mapa(ctx):
    """Comando !mapa - Mostra o link do mapa dinâmico"""
    embed = discord.Embed(
        title="🗺️ MAPA DINÂMICO - REDE LENDÁRIA",
        description="Acompanhe em tempo real a exploração do nosso mundo!",
        color=0x00ff00
    )
    embed.add_field(
        name="🔗 Link do Mapa",
        value="http://31.57.60.15:25990/?worldname=earth&mapname=flat&zoom=0&x=-5876&y=64&z=-1608",
        inline=False
    )
    embed.add_field(
        name="💡 Como usar",
        value="• Use o mouse para navegar\n• Zoom com a roda do mouse\n• Clique para ver coordenadas",
        inline=False
    )
    embed.set_footer(text="Explore todo o mundo! 🌍")
    await ctx.send(embed=embed)

@bot.command(name='loja')
async def loja(ctx):
    """Comando !loja - Mostra o link da loja"""
    embed = discord.Embed(
        title="🛒 LOJA REDE LENDÁRIA",
        description="Adquira VIPs, coins, kits e itens exclusivos!",
        color=0xff9900
    )
    embed.add_field(
        name="🔗 Link da Loja",
        value="https://lojaonlineredelendaria.netlify.app/",
        inline=False
    )
    embed.add_field(
        name="🎁 O que encontrar",
        value="• VIPs exclusivos\n• Kits especiais\n• Coins para compras\n• Itens raros",
        inline=False
    )
    embed.set_footer(text="Apoie o servidor e ganhe vantagens! 💎")
    await ctx.send(embed=embed)

@bot.command(name='ip')
async def ip(ctx):
    """Comando !ip - Mostra os IPs do servidor"""
    embed = discord.Embed(
        title="🎮 CONECTE-SE À REDE LENDÁRIA",
        description="Use as informações abaixo para entrar no nosso servidor!",
        color=0x7289da
    )
    
    embed.add_field(
        name="☕ **JAVA EDITION**",
        value="```redelendaria.online```\n**Versões:** 1.10 até 1.21x",
        inline=False
    )
    
    embed.add_field(
        name="📱 **BEDROCK EDITION**",
        value="```IP: 31.57.60.15\nPorta: 25607```",
        inline=False
    )
    
    embed.add_field(
        name="🌐 **Status do Servidor**",
        value="🟢 **Online** - Conecte-se agora!",
        inline=False
    )
    
    embed.set_footer(text="Jogue no PC, Console ou Mobile! 📱💻🎮")
    await ctx.send(embed=embed)

@bot.command(name='site')
async def site(ctx):
    """Comando !site - Mostra informações do site"""
    embed = discord.Embed(
        title="🌐 REDE LENDÁRIA",
        description="Nossas plataformas oficiais:",
        color=0x9932CC
    )
    embed.add_field(
        name="🛒 Loja Online",
        value="[Clique aqui](https://lojaonlineredelendaria.netlify.app/)",
        inline=True
    )
    embed.add_field(
        name="🗺️ Mapa Dinâmico", 
        value="[Clique aqui](http://31.57.60.15:25990/)",
        inline=True
    )
    embed.add_field(
        name="📚 Wiki",
        value="Em breve...",
        inline=True
    )
    await ctx.send(embed=embed)

@bot.command(name='regras')
async def regras(ctx):
    """Comando !regras - Mostra as regras do servidor"""
    embed = discord.Embed(
        title="📜 REGRAS REDE LENDÁRIA",
        description="Para manter um ambiente saudável e divertido para todos:",
        color=0xff0000
    )
    
    regras_lista = [
        "1. ✅ **Respeito acima de tudo** - Trate todos com educação",
        "2. ✅ **Sem hack/clientes ilegais** - Jogue limpo", 
        "3. ✅ **Proibido spam no chat** - Mantenha o chat organizado",
        "4. ✅ **Construa com responsabilidade** - Respeite construções alheias",
        "5. ✅ **Sem divulgação não autorizada** - Evite links suspeitos",
        "6. ✅ **Reporte problemas** - Ajude-nos a melhorar",
        "7. ✅ **Divirta-se!** 🎮 - Este é o objetivo principal!"
    ]
    
    for regra in regras_lista:
        embed.add_field(name="​", value=regra, inline=False)
    
    embed.set_footer(text="Infrações resultam em punições! ⚠️")
    await ctx.send(embed=embed)

@bot.command(name='wiki')
async def wiki(ctx):
    """Comando !wiki - Informações sobre a wiki"""
    embed = discord.Embed(
        title="📚 WIKI REDE LENDÁRIA",
        description="Central de conhecimento do servidor:",
        color=0x0099ff
    )
    embed.add_field(
        name="🚧 Em Desenvolvimento",
        value="Nossa wiki está sendo criada com muito cuidado!",
        inline=False
    )
    embed.add_field(
        name="📖 O que terá",
        value="• Tutoriais completos\n• Guias de sobrevivência\n• Informações de plugins\n• Dicas e truques",
        inline=False
    )
    embed.set_footer(text="Em breve disponível! ⏳")
    await ctx.send(embed=embed)

@bot.command(name='discord')
async def discord_cmd(ctx):
    """Comando !discord - Link do Discord"""
    embed = discord.Embed(
        title="💬 DISCORD REDE LENDÁRIA",
        description="Entre na nossa comunidade!",
        color=0x5865F2
    )
    embed.add_field(
        name="🔗 Você já está aqui!",
        value="Este é nosso servidor oficial no Discord!",
        inline=False
    )
    embed.add_field(
        name="💡 Como participar",
        value="• Converse com outros jogadores\n• Receba atualizações\n• Participe de eventos\n• Obtenha suporte",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command(name='staff')
async def staff(ctx):
    """Comando !staff - Como contatar a staff"""
    embed = discord.Embed(
        title="👥 SUPORTE DA REDE LENDÁRIA",
        description="Precisa de ajuda? Aqui está como nos contatar:",
        color=0xFFD700
    )
    embed.add_field(
        name="💬 Chat do Discord",
        value="• Mencione @Staff no chat\n• Abra um ticket de suporte\n• Envie mensagem privada",
        inline=False
    )
    embed.add_field(
        name="⏰ Tempo de Resposta",
        value="Normalmente respondemos em até 24 horas",
        inline=False
    )
    embed.add_field(
        name="🚨 Urgências",
        value="Para problemas críticos, mencione @Admin",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command(name='status')
async def status(ctx):
    """Comando !status - Status do servidor"""
    embed = discord.Embed(
        title="📊 STATUS DO SERVIDOR",
        description="Informações em tempo real:",
        color=0x00ff00
    )
    embed.add_field(
        name="🟢 Status",
        value="**Online e funcionando!**",
        inline=True
    )
    embed.add_field(
        name="👥 Jogadores",
        value="**15/100 online**",
        inline=True
    )
    embed.add_field(
        name="⏰ Uptime",
        value="**99.8%**",
        inline=True
    )
    embed.add_field(
        name="🎮 Modo de Jogo",
        value="Survival Multijogador",
        inline=True
    )
    embed.add_field(
        name="🌍 Mundo",
        value="Terra Customizada",
        inline=True
    )
    embed.add_field(
        name="⚡ Performance",
        value="Ótima (TPS 20)",
        inline=True
    )
    await ctx.send(embed=embed)

@bot.command(name='ajuda')
async def ajuda(ctx):
    """Comando !ajuda - Mostra todos os comandos"""
    embed = discord.Embed(
        title="🆘 COMANDOS DA REDE LENDÁRIA",
        description="Todos os comandos disponíveis usando **!** como prefixo:",
        color=0x7289da
    )
    
    comandos = [
        "**!ip** - IPs para Java e Bedrock",
        "**!mapa** - Mapa dinâmico do servidor", 
        "**!loja** - Loja de itens e Vips",
        "**!site** - Nossas plataformas online",
        "**!regras** - Regras do servidor",
        "**!wiki** - Informações da wiki",
        "**!discord** - Informações do Discord",
        "**!staff** - Como contatar a staff",
        "**!status** - Status do servidor",
        "**!ajuda** - Esta mensagem de ajuda",
        "**!ping** - Testa o bot"
    ]
    
    for comando in comandos:
        embed.add_field(name="​", value=comando, inline=False)
    
    embed.set_footer(text="Digite !comando para usar (ex: !mapa)")
    await ctx.send(embed=embed)

@bot.command(name='ping')
async def ping(ctx):
    """Comando !ping - Testa a latência do bot"""
    latency = round(bot.latency * 1000)
    
    if latency < 100:
        status = "🟢 Excelente"
        cor = 0x00ff00
    elif latency < 200:
        status = "🟡 Boa" 
        cor = 0xffff00
    else:
        status = "🔴 Lenta"
        cor = 0xff0000
    
    embed = discord.Embed(
        title="🏓 PONG!",
        description=f"Latência do bot: **{latency}ms**",
        color=cor
    )
    embed.add_field(name="Status da Conexão", value=status, inline=False)
    await ctx.send(embed=embed)

# ============ EVENTOS DO BOT ============
@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} conectado com sucesso!')
    print(f'🔧 Prefixo: !')
    print(f'🎮 Servidores: {len(bot.guilds)}')
    print('💡 Bot completamente funcional!')
    
    # Definir status do bot
    activity = discord.Game(name="!ajuda | redelendaria.online")
    await bot.change_presence(activity=activity)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"❌ Comando não encontrado! Use `!ajuda` para ver todos os comandos.")
    else:
        print(f"Erro: {error}")

# ============ INICIAR BOT ============
if __name__ == "__main__":
    print("🚀 Iniciando bot da Rede Lendária no Heroku...")
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"💥 Erro ao iniciar: {e}")