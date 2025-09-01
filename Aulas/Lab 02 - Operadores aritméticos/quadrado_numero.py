'''
Escreva um programa em python que receba três números inteiros quaisquer e apresente:
a) a soma dos quadrados dos três números;
b) o quadrado da soma dos três números.
'''

import math

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = int(input("Digite um número inteiro: "))

soma_quadrado = (math.pow(n1,2)+math.pow(n2,2)+math.pow(n3,2))
quadrado_soma = math.pow((n1+n2+n3),2)

print ("A soma dos quadrados dos três números: ", soma_quadrado)
print ("O quadrado da soma dos três números: ", quadrado_soma)

