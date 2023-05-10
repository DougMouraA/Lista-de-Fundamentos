for i in range(5):
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    if A > B:
        print("Nao e possivel mostrar os numeros pares entre A e B")
    else:
        for j in range(A, B+1):
            if j % 2 == 0:
                print(j)
