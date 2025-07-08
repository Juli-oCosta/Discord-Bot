import os
from dotenv import load_dotenv
import discord 
from discord import app_commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class Bot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="!",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self):
        await self.tree.sync()
    
    async def on_ready(self):
        print(f"O Bot {self.user} entrou na conversa.")
    
bot = Bot()

@bot.tree.command(name="cumprimento_usuário", description="Faz uma saudação ao usuário que o chamar.")
async def falaUsuario(interaction:discord.Interaction):
    await interaction.response.send_message(f"Fala ae {interaction.user.mention}, ta tudo sussa?")

@bot.tree.command(name="soma", description="Some dois números.")
@app_commands.describe(
    num1 = "Primeiro número a somar.",
    num2 = "Segundo número a somar." 
)
async def somaNumeros(interaction:discord.Interaction, num1:int, num2:int):
    resultado = num1 + num2
    mensagem = f"A opa {interaction.user.mention} o negócio é o seguinte, falaro que {num1} + {num2} = {resultado}"
    if resultado == 24:
        mensagem += " (viisheee)"
        
    await interaction.response.send_message(mensagem, ephemeral=True)
    
# For safety reasons, the token should not be shared.
# Por questões de segurança, o token não deve ser compartilhado
bot.run(TOKEN)
