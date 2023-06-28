def criarMatriz(mat):
    for i in range(0,4):
        mat.append(0)
        mat[i] = []
        for j in range(0, 4):
            mat[i].append(j)
    return mat

def busca(mat, x):
    achou = False
    for i in range(0, 4):
        for j in range(0, 4):
            if mat[i][j] == x:
                achou = True
                return print(i, j)
    if achou == False:
        return print("Elemento nao encontrado")
    
mat = []
mat = criarMatriz(mat)
for i in range(0, 4):
    for j in range(0, 4):
        print(mat[i][j], end=" ")
    print()
x = int(input("Valor a buscar: "))
busca(mat, x)
