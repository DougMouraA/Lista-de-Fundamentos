def calcularNotas(gabarito, respostas):
    notas = []
    for aluno in respostas:
        nota = 0
        for i in range(len(gabarito)):
            if gabarito[i] == aluno[i]:
                nota += 1
        notas.append(nota)
    return notas

# Leitura do vetor gabarito
gabarito = []
for i in range(1, 6):
    resposta = input(f"Informe a resposta correta para a questão {i}: ")
    gabarito.append(resposta)

# Leitura da matriz de respostas
respostas = []
for i in range(40):
    aluno = []
    for j in range(1, 6):
        resposta = input(f"Informe a resposta do aluno {i+1} para a questão {j}: ")
        aluno.append(resposta)
    respostas.append(aluno)

# Cálculo das notas dos alunos
notas = calcularNotas(gabarito, respostas)

# Impressão das notas dos alunos
for i in range(len(notas)):
    print(f"Nota do aluno {i+1}: {notas[i]}")
