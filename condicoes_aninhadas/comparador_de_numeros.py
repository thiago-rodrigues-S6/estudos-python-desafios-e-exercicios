#Comparando dois numeros

from time import sleep

numero1 = int(input(" \033[0;34m Digite o primeiro Número: "))
numero2 = int(input(" \033[0;33m Digite o segundo Número: "))

print("\n \033[0m analisando numeros.... ")
sleep(3)

if numero1 > numero2:
  print("\n \033[0;34m o Número {} é maior do que o numero {}, portanto. numero 1 ganha. \033[m".format(numero1, numero2))
elif numero2 > numero1:
  print("\n \033[0;33m o Número {} é maior do que o numero {}, portanto. numero 2 ganha. \033[m".format(numero2, numero1))
else:
  print("\n \033[0m Os dois numeros sao iguais, então nenhum número ganhará. ")
