polegada = float(input("valor em polegadas: "))
verify = True
while verify != False:
    if polegada > 0:
        cm = polegada * 2.54
        print(polegada,"pol = ",cm,"cm.")
        verify = False
    else:
        print("Insira um valor valido.")
        polegada = float(input("valor em polegadas: "))
