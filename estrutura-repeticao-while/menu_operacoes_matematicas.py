from time import sleep
opcao = 0

numero1 = int (input(" \n Digite o primeiro numero: "))
numero2 = int (input(" Digite o segundo numero: "))

while opcao != 5:

  print(" \n O que você deseja fazer com esses dois números? ")
  print(" [1] Somar. ")
  print(" [2] Multiplicar. ")
  print(" [3] Maior. ")
  print(" [4] novos números. ")
  print(" [5] Sair do programa. ")

  opcao = int (input(" Digite a opção desejada: "))

  if opcao == 1:
    print(" \n A Soma do numero {} com o numero {} é de {} ".format(numero1, numero2 , numero1 + numero2))
  elif opcao == 2:
    print(" \n A multiplicação do numero {} com o numero {} é de {} ".format(numero1 , numero2 , numero1 * numero2))
  elif opcao == 3:
    if numero1 > numero2:
      print(" \n o maior numero é {} e o menor acaba sendo {}. ".format(numero1 , numero2))
    elif numero2 > numero1:
      print(" \n o maior numero é {} e o menor acaba sendo {}. ".format(numero2 , numero1))
    else:
      print(" \n Ambos os numeros são iguais não sendo maior e nem menor. ")
  elif opcao == 4:
      print("\n Informe os numeros novamente: ")
      numero1 = int (input("Primeiro valor: "))
      numero2 = int (input("Segundo valor: "))
  elif opcao == 5:
     print(" \n Encerrando o programa...")
     sleep(5)
     print(" \033[1;32m Até a próxima. :) \033[0m ")
  else:
    print(" \n \033[4;31m a opcao {} que voce digitou não existe no menu, tente novamente. \033[0m ".format(opcao))
