m = int(input("m: "))
n = int(input("n: "))
while n >= m:
    print("insira um valor para n que seja maior que m (", m,")")
    n = int(input("n: "))
lado1 = (m**2) - (n**2)
lado2 = 2 * m * n
hipo = (m**2) + (n**2)
print("Lado 1 =", lado1,", lado 2 =",lado2,", hipotenusa =",hipo)
