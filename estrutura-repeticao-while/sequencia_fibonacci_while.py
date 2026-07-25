## Calculando fibonnaci 2

termos = int(input("quantos termos você quer? "))
contador = numero = 0
inicio = 1

while contador < termos:

  contador +=1
  fibonacci = inicio + numero
  inicio = numero
  numero = fibonacci
  if inicio == 0:
    print(inicio , end = " > ")
  else:
    print(inicio , end = " > ")
    print("FIM " if contador == termos else "" , end = "")
