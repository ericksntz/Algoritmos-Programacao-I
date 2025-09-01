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
