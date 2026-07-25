mulheres = 0
soma_idades = 0
maior_idade = 0

for c in range (4):
  nome = (input("\n Digite o seu nome. "))
  idade = int(input(" Digite sua idade. "))
  print(" Você é masculino ou feminino? ")
  sexo = (input(" Digite M para masculino ou F para feminino. ")).strip().lower()
  soma_idades = soma_idades + idade

  if sexo == "M".lower():
    if maior_idade < idade:
       maior_idade = idade
       nome_maior_idade = nome

  if sexo == "F".lower():
    mulheres = mulheres + 1

print(" \n \033[0;31m O total de mulheres contado nesse grupo é de {} mulheres. ".format(mulheres))
print(" \033[4 ;34m O homem mais velho desse grupo é o {} com {} anos. ".format(nome_maior_idade, maior_idade))

media = soma_idades // 4

print(" \033[0;33m A média da idade do grupo é de {} anos. ".format(media))
