mat = []
somapar = 0
for i in range(0,3):
    mat.append(0)
    mat[i] = []
    for j in range(0, 3):
        mat[i].append(int(input("Digite um valor: ")))
        if mat[i][j] % 2 == 0:
            somapar += mat[i][j]
print(mat)
print(somapar)
