'''
Escreva um programa em python que solicite ao usuário a distância entre duas cidades (em Km) e o
tempo de viagem (em horas). O programa deverá calcular e exibir a velocidade média da viagem.
Utilize a fórmula: Velocidad Média = Distância / Tempo
'''

distancia = float(input("Digite a distância entre duas cidades (em Km): "))
tempo = float(input("Digite o tempo da viagem (em horas): "))

velocidade = distancia/tempo

print (f"A velocidade média da viagem é: {velocidade:.2f}km/h")