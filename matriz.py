def create_matrix(rows, cols):
    matrix = [[0] * cols for _ in range(rows)]  # Inicializa a matriz com zeros

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Verifica se os elementos ao redor são iguais a 0
            if (
                matrix[i-1][j] == 0 and
                matrix[i+1][j] == 0 and
                matrix[i][j-1] == 0 and
                matrix[i][j+1] == 0
            ):
                matrix[i][j] = 7  # Define o valor 7 no elemento atual

    return matrix

rows = 5
cols = 5

matrix = create_matrix(rows, cols)

# Imprime a matriz resultante
for row in matrix:
    print(row)
