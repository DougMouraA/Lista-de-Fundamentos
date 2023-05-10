nota1 = float(input("nota 1: "))
p1 = float(input("peso da nota 1: "))
nota2 = float(input("nota 2: "))
p2 = float(input("peso da nota 2: "))
nota3 = float(input("nota 3: "))
p3 = float(input("peso da nota 3: "))
total_n_p = nota1*p1 + nota2*p2 + nota3*p3
total_p = p1 + p2 + p3
media = total_n_p / total_p
print("A media ponderada do aluno(a):", media)
