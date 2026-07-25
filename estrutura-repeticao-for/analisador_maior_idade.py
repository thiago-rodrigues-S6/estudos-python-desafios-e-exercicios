maior_idade = 0
menor_idade = 0
soma_maior_idade = 0
soma_menor_idade = 0

for c in range(0,3):
  idade = int(input("Digite sua idade. "))

  if idade >=18:
    maior_idade = maior_idade + 1
    soma_maior_idade = soma_maior_idade + idade
  else:
    menor_idade = menor_idade + 1
    soma_menor_idade = soma_menor_idade + idade

print(" \033[0;31m nessa lista tem {} pessoas maiores de idade ".format(maior_idade) ,end ="")
print("e a soma das idades é de {} ".format(soma_maior_idade))
print(" \033[0;34m nessa lista tem {} pessoas menores de idade ".format(menor_idade),end ="")
print("\033[0;33m e a soma das idades é de {} ".format(soma_menor_idade))
