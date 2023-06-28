def criarVetor(vet):
    n = 0
    for i in range(0, TAM):
        n = float(input("Digite a nota do aluno: "))
        vet[i] = n
    return vet

def mediaAluno(vet):
    soma = 0
    for i in range(0, TAM):
        soma += vet[i]
    media = soma / TAM
    return media

def qtdAlunoAR(vet, media):
    contA = 0
    contR = 0
    for i in range(0, TAM):
        if vet[i] >= media:
            contA += 1
        else:
            contR += 1
    return contA, contR

TAM = 10
vet = [0]*TAM
vet = criarVetor(vet)
media = 0
media = mediaAluno(vet)
aprovados, reprovados = qtdAlunoAR(vet, media)

print("A media da turma foi de", media,"onde", aprovados,"alunos tiveram nota\
acima da media e", reprovados,"alunos tiveram nota abaixo da media")
