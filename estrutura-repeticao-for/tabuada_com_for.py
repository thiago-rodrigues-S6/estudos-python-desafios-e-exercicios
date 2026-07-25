#fazendo a tabuada com for

numero = int(input(" Digite um número. "))
print(" \n \033[0;33m A SEGUIR A TABUADA DO NUMERO {} \033[0;0m".format(numero))
print("")

for c in range(1,10+1):
  resultado = numero * c
  print(" \033[0;34m " , numero , "x" , c  , "=", resultado)
