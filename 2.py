import math

def distancia():
    x1 = float(input("Digite a coordenada x do primeiro ponto: "))
    y1 = float(input("Digite a coordenada y do primeiro ponto: "))

    x2 = float(input("Digite a coordenada x do segundo ponto: "))
    y2 = float(input("Digite a coordenada y do segundo ponto: "))

    conta = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return conta

resultado = distancia()
print(f"A distância entre os pontos é: {resultado}")