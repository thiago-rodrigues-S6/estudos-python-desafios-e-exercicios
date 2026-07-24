## Programa para ler ângulos

from math import radians, sin, cos, tan, sqrt

comprimento = float(input("Digite o comprimento do cateto oposto "))
comprimentoca = float(input("Digite o comprimento do cateto adjacente "))
soma= comprimento + comprimentoca
hipotenusa = sqrt(comprimento **2 + comprimentoca **2 )

print("a soma dos catetos é {} e o comprimento da hipotenusa é {:.3f} ".format(soma, hipotenusa ))

angulo = float(input("\n Digite o valor do angulo "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O valor do Seno {:.3f} o Cosseno {:.3f} e a tangente {:.3f} ".format(seno, cosseno, tangente))