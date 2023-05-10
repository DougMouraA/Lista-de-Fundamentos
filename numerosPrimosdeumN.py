
n = int(input("Digite um numero: "))
if n == 1:
    print("Nao e primo")
elif n == 2:
    print (n)
else:
    for i in range(1, n+1):
        cont = 0
        primo = False
        for j in range(2, i):
            if(i % j == 0):
                cont += 1
            if cont == 0 and j != 1:
                primo = True
        if primo == True:
            print(i)
