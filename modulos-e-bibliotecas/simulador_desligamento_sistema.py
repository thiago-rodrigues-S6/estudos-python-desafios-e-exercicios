import time

print("preparando para desligar o sistema... ")
print("=====")

#aqui faz uma contagem de 3 a 1 
for c in range(3, 0, -1):
  print(f" {c}... ")
  time.sleep(1) #pausa de 1 segundo para cada número

print("=====")
print("O sistema está pronto para ser desligado...")
time.sleep(3)
print("Tchau... até a próxima... :) ")