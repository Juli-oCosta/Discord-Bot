# Imports básicos para o funcionamento do código
import random
from datetime import date
import datetime

# Importando as mensagens dos cablocos
from mensagens import mensagens_sex_ta
from mensagens import mensagens_quinta
from mensagens import mensagens_aviso

global contagem_sex_ta
contagem_sex_ta = 0

global dia_atual
dia_atual = datetime.date.today()
ano, semana, dia_da_semana = dia_atual.isocalendar()

# Caso o dia da semana for sex ta-feira, os cablocos avisam a gente por mensagem
if dia_da_semana == 5:
    contagem_sex_ta = contagem_sex_ta + 1
    print()
elif dia_da_semana == 4:
    print()