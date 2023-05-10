area = 0
largura = float(input("Largura: "))
while largura > 0:
    comp = float(input("Comprimento: "))
    areap = largura * comp
    area += areap
    largura = float(input("Largura: "))
if area > 0:
    print("Area total:", area)
