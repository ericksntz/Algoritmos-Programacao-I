import math

altura = float(input("Entre com a altura: "))
raio = float(input("Entre com o raio: "))

volume = math.pi*(math.pow(raio,2)*altura)

print (f"Volume: {volume:.2f}")
