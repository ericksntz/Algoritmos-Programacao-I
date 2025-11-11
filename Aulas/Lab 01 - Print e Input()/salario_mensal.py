"""
Escreva um programa em python que pergunte ao empregado da
empresa “MG System” quanto ele ganha por hora trabalhada (número
inteiro) e o número de horas (número inteiro) que ele trabalhou no mês.
Calcule e mostre o salário a receber no referido mês.
"""

valor_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas_mes = int(input("Digite quantas horas horas trabalhadas no mês: "))

salario = valor_hora*horas_trabalhadas_mes

print ("Seu salário esse mês é: R$", salario)
