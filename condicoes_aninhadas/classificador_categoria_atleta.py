# Classificando dados de confederação de natação

ano_nascimento = int(input("Digite o seu ano de nascimento. "))
ano_atual = int(input("Digite o ano atual. "))

idade = ano_atual - ano_nascimento

if idade <= 9:
  print("\033[0;32m Você tem {} anos. está classificado na categoria MIRIM. ".format(idade))
elif idade <= 14:
  print("\033[0;33m Você tem {} anos. está classificado na categoria INFANTIL. ".format(idade))
elif idade <= 19:
  print("\033[0;34m Você tem {} anos. está classificado na categoria JUNIOR. ".format(idade))
elif idade == 20:
  print("\033[1;30;47m Você tem {} anos. está classificado na categoria SÊNIOR. ".format(idade))
elif idade >= 21:
  print("\033[35m Você tem {} anos. está classificado na categoria MASTER. ".format(idade))