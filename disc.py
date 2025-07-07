import discord
from discord import app_commands

class MeuPrimeiroBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="!",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync

    async def on_ready(self):
        print(f"O bot {self.user} foi ligado com sucesso.")

bot = MeuPrimeiroBot()

@bot.tree.command(name="olá-usuário", description="Primeiro comando do bot.")
async def olamundo(interaction:discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.mention}!")

@bot.tree.command(name="soma", description="Some dois números distintos.")
@app_commands.describe(
    numero1 = "Primeiro número a somar.",
    numero2 = "Segundo númeroa somar."
)
async def somaNumero(interaction:discord.Interaction, numero1:int, numero2:int):
    numero_somado = numero1 + numero2
    await interaction.response.send_message(f"O número somado é: {numero_somado}", ephemeral=True)

# For safety reasons, the token should not be shared.
# Por questões de segurança, o token não deve ser compartilhado
bot.run("") # token
