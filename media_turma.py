for i in range(2):
    i = input("Nome da turma: ")
    alunos = 0
    nota_turma = 0
    for j in range(5):
        j = input("Nome do aluno: ")
        n1 = float(input("Primeira nota: "))
        n2 = float(input("Segunda nota: "))
        media = (n1 + n2)/2
        if media >= 7:
            print("Aluno",j,"está aprovado com media",media)
        else:
            print("Aluno",j,"está reprovado com media",media)
        alunos +=1
        nota_turma += media
    media_turma = nota_turma / alunos
    print("A media da turma",i,"e",media_turma)
