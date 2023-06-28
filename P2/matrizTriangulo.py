def criarMatriz(mat):
    for i in range(0, 10):
        mat.append(0)
        mat[i] = []
        for j in range(0, 3):
            mat[i].append(int(input("n: ")))
    return mat

def perimetro(mat, vet):
    for i in range(0, len(mat)):
        soma = 0
        for j in range(0, len(mat[i])):
            soma += mat[i][j]
        vet[i] = soma
    return vet
        

mat = []
mat = criarMatriz(mat)
for i in range(0, 10):
    for j in range(0, 3):
        print(mat[i][j], end=" ")
    print()
vet = [0.0]*10
vet = perimetro(mat, vet)
print(vet)
