a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))
if a == 0:
    print("Essa equacao nao eh de seguno grau")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("A equacao nao tem raizes reais")
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("As raizes sao:", x2,",", x1)
