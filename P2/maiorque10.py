def criarMatriz(mat):
    for i in range(0, 6):
        mat.append(0)
        mat[i] = []
        for j in range(0, 6):
            mat[i].append(int(input("Digite um valor: ")))
    return mat

def maiorDez(mat):
    cont = 0
    for i in range(0, 6):
        for j in range(0, 6):
            if mat[i][j] > 10:
                cont += 1
    return cont


mat = []
mat = criarMatriz(mat)
for i in range(0, 6):
    for j in range(0, 6):
        print(mat[i][j], end=" ")
    print()
maior = maiorDez(mat)
print(maior)

