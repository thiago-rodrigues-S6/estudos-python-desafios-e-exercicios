#Lendo apenas os números pares.

from time import sleep

resultado = 0
impar = 0

for contador in range(0,6):
  numero = int(input("Digite um número. "))

  if numero % 2 == 0:
    resultado = resultado + numero
  else:
    impar += numero

print("\n Calculando os números encontrados.....")
sleep(4)

print("\n \033[0;32m A soma dos numeros pares do laço é de {} ".format(resultado))
print("\n \033[0;31m A soma dos numeros impares é de {} ".format(impar))