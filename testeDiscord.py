import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # precisa ativar isso pra ler mensagens

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}!')

@bot.command()
async def oi(ctx):
    await ctx.send(f'Fala fiot, {ctx.author.name}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'gepetê' in message.content.lower():
        await message.channel.send('E aí fiot, chamou?')
    
    await bot.process_commands(message)

bot.run('SEU_TOKEN_AQUI')
