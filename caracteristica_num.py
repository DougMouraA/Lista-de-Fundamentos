n = int(input("Digite um numero entre 1000 e 9999: "))
mc = n // 100
du = n % 100
r = (mc + du)**2
if r == n:
    print("O numero", n,"obedece a caracteristica e o resultado e",r)
else:
    print("O numero,",n,"nao obedece a caracteristica e o resultado e",r)
