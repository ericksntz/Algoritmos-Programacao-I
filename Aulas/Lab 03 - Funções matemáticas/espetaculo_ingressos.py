"""
Faça um programa em python que receba o custo de um espetáculo teatral e o preço do ingresso
desse espetáculo. Esse programa deve calcular e mostrar:

a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo
seja alcançado.

b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.
Observações:

- nesta questão você poderá utilizar a função math.ceil(x) que retorna o menor inteiro maior ou igual
a x como int
"""

import math

custo_espetaculo = int(input("Digite o custo do espetáculo: "))
custo_ingresso = int(input("Digite o preço do ingresso: "))

minimo_ingresso = custo_espetaculo / custo_ingresso
minimo_ingresso = math.ceil(minimo_ingresso)

lucro = custo_espetaculo * 1.23

qtd_ingressos_lucro = lucro / custo_ingresso
qtd_ingressos_lucro = math.ceil(qtd_ingressos_lucro)

print ("Mínimo de ingressos: R$", minimo_ingresso)
print ("Lucro esperado de 23%: R$", lucro)
print ("Ingressos para ter lucro de 23%: ", qtd_ingressos_lucro)
