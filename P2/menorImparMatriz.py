def criarMatriz(mat):
    for i in range(0, 5):
        mat.append(0)
        mat[i] =[]
        for j in range(0, 5):
            mat[i].append(j)
    return mat

def menor(mat):
    soma = 0
    menor = mat[0][0]
    for i in range(0, 5):
        for j in range(0, 5):
            if mat[i][j] % 2 != 0:
                if menor % 2 == 0:
                    menor = mat[i][j]
                    soma = i + j
                if mat[i][j] < menor:
                    menor = mat[i][j]
                    soma = i + j             
    if menor % 2 == 0:
        return -1
    else:
        return soma
                
    
mat = []
mat = criarMatriz(mat)
for i in range(0, 5):
    for j in range(0, 5):
        print(mat[i][j], end=" ")
    print()
print(menor(mat))
