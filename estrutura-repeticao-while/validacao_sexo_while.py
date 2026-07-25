# lendo o sexo
sexo = ""

while sexo != "f" and sexo != "m":

  print(" \n \033[1;33m Qual é o seu genero? \033[0m ")
  sexo = (input(" \n  Digite M para masculino ou F para feminino. ")).strip().lower()

  if sexo != "f" and sexo != "m":
    print(" \n \033[4;31m Você digitou o seu gênero errado, tente novamente. \033[0m")

# Essas condições funcionaram fora do laço. ou seja só vão funcionar quando o while
# for verdade

if sexo == "f":
  sexo = "feminino"
  print(" \n \033[1;31m Você é uma mulher do gênero {}.".format(sexo))
else:
  sexo = "masculino"
  print(" \n \033[1;34m Você é um homem do gênero {}. ".format(sexo))