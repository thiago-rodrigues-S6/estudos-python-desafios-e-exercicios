#Jogando jokenpô com o computador

import random
import time

opções = ["pedra" , "papel" , "tesoura"]
escolha_usuario = str(input("Digite a sua escolha. ")).strip().lower()
escolha_computador = random.choice(opções)

print("\n escolhendo minha opçao....... ")
sleep (3)
print("minha escolha foi {} ".format(escolha_computador))

#condições de escolhas do computador.

if escolha_usuario == escolha_computador:
  print(" \n \033[33m Empatamos, precisaremos sortear de novo... ")
elif (escolha_usuario == "pedra" and escolha_computador =="papel") or (escolha_usuario == "tesoura" and escolha_computador == "papel"):
  if escolha_usuario == "pedra":
    print("\n \033[31m Papel ganha de pedra. portanto eu ganhei.")
  else:
    print("\n \033[32m Tesoura ganha de papel. então você ganhou. PARABÉNS. ")
elif escolha_usuario == "tesoura" or escolha_usuario == "papel" and escolha_computador == "pedra":
  if escolha_usuario == "tesoura":
    print("\n \033[31m Pedra ganha de tesoura. portanto eu ganhei. ")
  else:
    print("\n \033[32m Papel ganha de pedra. então você ganhou. PARABÉNS. ")
elif escolha_usuario == "papel" or escolha_usuario == "pedra" and escolha_computador == "tesoura":
  if escolha_usuario == "papel":
    print("\n \033[31m Tesoura ganha de papel, portanteo eu ganhei. ")
  else:
    print("\n \033[32m pedra ganha de tesoura, então você ganhou PARABÈNS. ")
else:
  print("\n \033[31m Escolha invalida tente novamente. ")