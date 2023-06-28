mat = []
soma = 0
for i in range(0,3):
    mat.append(0)
    mat[i] = []
    for j in range(0,3):
        mat[i].append(int(input("Digite um valor: ")))
        if i == j:
            soma += mat[i][j]
print(mat)
print(soma)
