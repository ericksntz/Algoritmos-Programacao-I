"""
Faça um programa em python que calcule e apresente o volume de uma lata de óleo, sabendo-se a
altura e o raio (ambos em centímetros) ( 𝑣 = 𝜋. 𝑟)

Mostre o resultado com 2 casas decimais.
"""

import math

altura = float(input("Entre com a altura (em cm): "))
raio = float(input("Entre com o raio (em cm): "))

volume = math.pi*(math.pow(raio,2)*altura)

print (f"Volume: {volume:.2f}")
