## lendo PA

primeiro_numero = int(input("Digite o primeiro numero da PA."))
razao = int(input("Digite a razão dessa PA. "))

proximo_numero = 0

for c in range(1 , 11):
  proximo_numero = primeiro_numero + (c - 1) * razao
  print(proximo_numero)
