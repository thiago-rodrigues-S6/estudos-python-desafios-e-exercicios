#Lendo peso

maior_peso = 0
menor_peso = 0

for c in range(0,5):
  peso = float(input("\n Digite seu peso. " ))

  if c == 0:
    maior_peso = peso
    menor_peso = peso
  elif peso >= maior_peso:
    maior_peso = peso
    print(" O maior peso encontrado até agora é {} kilos ".format(peso))
  elif peso < menor_peso:
    menor_peso = peso
    print(" O menor peso encontrado até agora é {} kilos ".format(peso))
  else:
    print(" peso dentro da média")

print("\n \033[0;32m o maior peso encontrado no programa é o de {} kilos. ".format(maior_peso))
print("\033[0;34m  o menor peso encontrado no programa é o de {} kilos. ".format(menor_peso))