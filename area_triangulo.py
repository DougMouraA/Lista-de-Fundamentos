base = float(input("Informe a base: "))
largura = float(input("Informe a largura: "))
area = 0
if base > 0 and largura > 0:
    area = base * largura
    print(area)
else:
    print("Dados invalidos")
