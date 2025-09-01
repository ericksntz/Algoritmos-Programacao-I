"""
Três amigos, Carlos, André e Felipe, decidiram rachar igualmente a conta em um bar.
Faça um programa em python para ler o valor total da conta e imprimir quanto cada um deve pagar, mas
faça com que Carlos e André não paguem centavos. 
"""

total = float(input("Digite o valor total da conta: R$"))

parte_carlos_andre = total // 3
parte_felipe = (total - (parte_carlos_andre*2))

print (f"Total da conta: R${total:.2f}")
print (f"\nR${parte_felipe:.2f} para Felipe,")
print (f"R${parte_carlos_andre:.2f} para André e\nR${parte_carlos_andre:.2f} para Carlos")