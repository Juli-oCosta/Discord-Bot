# Imports básicos para o funcionamento do código
import random
from datetime import date
import datetime

# Importando as mensagens dos cablocos
from mensagens import mensagens_sex_ta
from mensagens import mensagens_quinta
from mensagens import mensagens_aviso

contagem_sex_ta = 0

dia_atual = datetime.date.today()
ano, semana, dia_da_semana = dia_atual.isocalendar()

# Caso o dia da semana for sex ta-feira, os cablocos avisam a gente por mensagem
# Tem q fazer com que o código rode apenas uma vez toda sex ta obviamente
# Tem q ser algo que fique ativo e guarde as informações, para contar quantas sex tas passaram para rodar a mensagem de aviso
if dia_da_semana == 5:
    contagem_sex_ta = contagem_sex_ta + 1
    print(random.choice(mensagens_sex_ta))
elif dia_da_semana == 4:
    print(random.choice(mensagens_quinta))

if contagem_sex_ta == 3 and dia_da_semana == 3:
    contagem_sex_ta = 0
    print(random.choice(mensagens_aviso))
