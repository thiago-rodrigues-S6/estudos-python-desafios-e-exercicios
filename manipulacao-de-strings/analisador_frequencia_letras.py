#Analisando frase

frase = "o dia estaria muito bonito atualmente".lower().strip()

print(frase[27])
print("a frase tem {} letras".format(len(frase)))
print("na frase existem  {}  letras 'A' ".format(frase.count("a")))
print("a primeira letra 'a' esta na posiçao: {} ".format(frase.find("a")))
print("a última letra 'a' esta na posiçao: {} ".format(frase.find("a" , 27 + 1 )))