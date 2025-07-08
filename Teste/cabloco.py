# bot_cabloco.py

import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv
import datetime
import random
import json

# --- CONFIGURAÇÃO INICIAL ---
# Carrega as variáveis do arquivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# Pega o ID do canal para onde as mensagens serão enviadas
CANAL_ID = int(os.getenv("CANAL_AVISOS_ID"))

# --- MENSAGENS ---
# (Você pode manter em um arquivo separado ou colocar aqui)
mensagens_sex_ta = [
    'É SEX TA!!',
    'Ê doido, dá uma bizoiada aí no calendário de vocês.'
]
mensagens_quinta = [
    'É amanhã',
    'Rapaz, nem conto pra vocês oq vem depois de hoje.',
    '*Cachorro robróquiu.'
]
mensagens_aviso = [
    'Fica de zóio aí que os cablocos falsos estão andando pelo Rosinha procurando vocês.',
    'Os cablocos falsos estão com fome, fica esperto, eles tão querendo cozinhar vocês.'
]

# --- FUNÇÕES PARA PERSISTÊNCIA DO CONTADOR ---
# Função para carregar o contador do arquivo
def carregar_contador():
    try:
        with open('contador.json', 'r') as f:
            data = json.load(f)
            return data.get('contagem_sex_ta', 0)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou estiver vazio, começa do zero
        return 0

# Função para salvar o contador no arquivo
def salvar_contador(contagem):
    with open('contador.json', 'w') as f:
        json.dump({'contagem_sex_ta': contagem}, f)

# --- CLASSE DO BOT ---
class Bot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f"O Bot {self.user} entrou na conversa.")
        # Inicia a tarefa agendada quando o bot estiver pronto
        self.verificar_dia.start()

    # Define uma tarefa que roda a cada 24 horas
    @tasks.loop(hours=24)
    async def verificar_dia(self):
        # Pega o objeto do canal usando o ID que definimos
        canal = self.get_channel(CANAL_ID)
        if not canal:
            print(f"Erro: Canal com ID {CANAL_ID} não encontrado.")
            return

        # Pega o dia da semana no formato isocalendar (Segunda=1, ..., Sexta=5, Domingo=7)
        hoje = datetime.date.today()
        dia_da_semana = hoje.isocalendar()[2]

        # Carrega a contagem atual do arquivo
        contagem_sex_ta = carregar_contador()

        # --- LÓGICA PRINCIPAL ---
        if dia_da_semana == 5: # Sexta-feira
            await canal.send(random.choice(mensagens_sex_ta))
            contagem_sex_ta += 1
            salvar_contador(contagem_sex_ta) # Salva o novo valor
            print(f"É sexta! Contagem atualizada para: {contagem_sex_ta}")

        elif dia_da_semana == 4: # Quinta-feira
            await canal.send(random.choice(mensagens_quinta))
            print("É quinta! Mensagem enviada.")

        # Verifica a condição do aviso especial
        if contagem_sex_ta >= 3 and dia_da_semana == 3: # Quarta-feira
            await canal.send(random.choice(mensagens_aviso))
            salvar_contador(0) # Reseta o contador e salva
            print("Aviso especial enviado! Contador resetado para 0.")

    # Garante que a tarefa comece apenas quando o bot estiver 100% conectado
    @verificar_dia.before_loop
    async def antes_de_verificar_dia(self):
        await self.wait_until_ready()


# --- INICIALIZAÇÃO ---
bot = Bot()
if TOKEN:
    bot.run(TOKEN)
else:
    print("Erro: Token do Discord não encontrado no arquivo .env")