a1 = int(input("Digite o primeiro termo da P.A :"))
r = int(input("Digite a razao da P.a: "))
n = int(input("Digite o numero de elementos da P.a: "))
for i in range(n):
    an = a1 + i * r
    print(an)
