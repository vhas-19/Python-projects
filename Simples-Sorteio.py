import os
import random
os.system('cls')

nomes= ["Huguinho", "Zezinho", "Luizinho", "Patricia"]


ganhador = random.choice(nomes)
print(f"Sorteio Simples: {ganhador}")
print(f"*" *48)
rodada = 1
while rodada <= 10:

    pesos = 10,10,10,70
    ganhador_peso=random.choices(nomes,weights=pesos, k=1)[0]
    print(f"Sorteio Rodada ({rodada}): {ganhador_peso}")
    rodada = rodada + 1