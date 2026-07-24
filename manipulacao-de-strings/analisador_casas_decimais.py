## contando de 0 a 9999

numero =  str (input("Digite um número: "))
numero = numero.zfill(4)
print("\nconvertendo o numero para leitura de casas....")
print("a conversão do número ficou:" , numero)

print(" \n A unidade desse numero é: {}".format(numero[3]))
print(" A dezena desse numero é: {}".format(numero[2]))
print(" A centena desse numero é: {}".format(numero[1]))
print(" A milhar desse numero é: {}".format(numero[0]))