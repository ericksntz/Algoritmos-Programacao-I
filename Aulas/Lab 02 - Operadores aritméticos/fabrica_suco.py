"""
A fábrica de suco Fit&Saudável vende seu produto em três formatos:
- lata de 350 ml
- garrafa de 600 ml
- garrafa de 2 litros (2000 ml)
Um comerciante compra uma determinada quantidade (valor inteiro) de cada formato de suco. Desenvolva
um programa, em python, que:
- solicite a quantidade de itens, de cada formato, que ele comprou;
- imprima na tela quantos litros (não é ml) de suco ele comprou no total;
- imprima na tela o total a pagar, considerando que cada litro custa R$ 9.50
"""

qtd_latas = int(input("Digite a quantidade de latas (350ml) compradas: "))
qtd_garrafa = int(input("Digite a quantidade de garrafas de (600ml) compradas: "))
qtd_garrafa_litro = int(input("Digite a quantidade de garrafas de (2 litros) compradas: "))

total_litros = (qtd_latas*0.35)+(qtd_garrafa*0.6)+(qtd_garrafa_litro*2000)/1000

total_pagar = (total_litros * 9.50)

print ("Total em litros de suco: ", total_litros)
print ("Total a pagar: ", total_pagar)

