# fazendo PA com o while

from time import sleep

# primeiro calculo do programa.

primeiro_termo = int(input("Escreva o primeiro termo da PA: "))
razao = int(input("Qual a razão dessa PA. "))
contador = 1

while contador <10:
  conta = (razao  * contador) + primeiro_termo
  if contador == 1:
    print(" \nOs 10 primeiros termos dessa PA são: ")
    print( primeiro_termo , end =" ")
  contador += 1
  print(conta , end = " ")

# criando variaveis para o segundo laço
termo_final1 = (razao * contador)
resposta = 1
resultado_final = 0

if contador == 10:
  while resposta > 0:
    resposta = int(input("\n Você quer ver mais quantos termos? "))
    if resposta >0:
      print(" \n Os proximos termos da PA que você pediu são esses: ")
      contador2 = 1
      while contador2 <= resposta:

        # criando condições pra executar a 1 volta e as demais.
        if resultado_final != 0:
          resultado = (razao * contador2) + resultado_final
          print(resultado , end = " ")
          contador2 += 1
        else:
          resultado = (razao * contador2) + termo_final1
          print(resultado , end = " ")
          contador2 += 1
    resultado_final = resultado
  else:
    print("\n Encerrando o programa... ")
    sleep(2)
    print(" \033[1;33m Então tá bom, até a proxima. :) ")
