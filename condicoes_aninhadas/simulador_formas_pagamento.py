#pagamento de um produto com diferentes casos.

valor_produto = float(input("Digite o valor do produto desejado. "))
escolha = str(input("Digite a forma de pagamento. ")).strip().lower()

print("\n \033[33m A forma de pagamento foi de {} ".format(escolha))

#Condições diferentes de pagamento.

if escolha == "dinheiro" or escolha == "cheque":
  print(" \n \033[0;32m O desconto será de 10% que será de {} R$ ".format(valor_produto * 0.10))
  print(" O valor final do produto será de  {} R$ ".format(valor_produto -(valor_produto * 0.10)))
elif escolha == "cartao":
  print(" \n \033[0;32m O desconto será de 5% que será de  {} R$ ".format(valor_produto * 0.05))
  print(" O valor final do produto será de {} R$ ".format(valor_produto - (valor_produto * 0.05)))
elif escolha == "2x no cartao":
  print(" \n \033[0;34m Aqui nessa opção não tem descontos. entao o preço será normal. ")
  print(" O valor das duas parcelas serão de {} R$ cada uma. ".format(valor_produto /2))
elif escolha == "3x no cartao":
  print(" \n \033[0;34m O juros será de 20% que vai ser de {} R$ ".format(valor_produto * 0.20))
  print(" O preço total do produto passa a ser de {} R$ ".format(valor_produto + (valor_produto * 0.20)))
  print(" Cada parcela terá o valor de {} R$ cada uma ".format((valor_produto + valor_produto *0.20)/3))
else:
  print(" \n \033[0;31m o Método de pagamento não foi reconhecido. tente novamente. ")