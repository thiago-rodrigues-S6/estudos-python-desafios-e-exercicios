# Fatorial com for

numero = int(input("Digite um numero. "))
fatorial = 1

for c in range (numero , 0 , -1):
  fatorial *= c
  print(fatorial , end = " ")

## em outra caixa de código 

# fatorial com while

numero = int(input("Digite um numero. "))
fatorial = numero

while numero > 0:

  numero -= 1
  fatorial *= numero

  if numero > 0:
    print(numero , " = " , fatorial)
