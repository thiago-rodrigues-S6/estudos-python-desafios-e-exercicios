#Jogo de adivinhação + while

import random
from time import sleep

escolha_usuario = 0
numero = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10)
escolhas_erradas = 0

computador = random.choice(numero)
print(computador)
print(" \033[1;33m Sorteando um numero.... \033[0m")
sleep(2)

while escolha_usuario != computador:

    escolha_usuario = int (input(" Escolha um numero de 1 a 10 "))

    if not (escolha_usuario ==  computador):
      escolhas_erradas += 1
      print("\n \033[1;31m Você errou tente novamente \033[0m")
    else:
      print("\n \033[1;32m VOCÊ ACERTOU PARABÉÉÉNSSSS!!! \033[0m")

print("Você precisou de {} tentativas para acertar o número sorteado. ".format(escolhas_erradas + 1))
