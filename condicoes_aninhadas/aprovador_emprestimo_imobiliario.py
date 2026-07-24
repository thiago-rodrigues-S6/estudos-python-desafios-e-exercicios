#Inicio do programa declarando variaveis e realizando algumas conversões
from time import sleep

valor_casa = float (input("\033[1;33m Qual o valor da casa que você vai comprar? \033[m"))
valor_salario = float(input(" Digite o valor de seu salário. "))
anos = int(input("Digite em quantos anos você vai querer fazer. "))
conversao_anos =  anos *  12
print("\n \033[0m Vai ser um total de {} meses. ".format(conversao_anos))
valor_parcelas = valor_casa // conversao_anos

#Colocando as condições agora do programa
print("\n Calculando o valor da parcela.... ")
sleep(5)

print("\n Vai ficar um total de {}R$ por mês.".format(valor_parcelas))
if valor_parcelas > valor_salario * 0.30:
  print("\033[1;31m O Valor da parcela excede o valor minimo do seu sálario" ,  end = " ")
  print("\n Portanto não será permitido continuar com a operação.")
else:
  print("\033[1;32m Parabéns o emprestimo logo será realizado na sua conta corrente. ")