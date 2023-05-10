p1_h = int(input("Horas aulas do professor 1: "))
p1_vh = float(input("Valor da hora aula do professor 1: "))
p2_h = int(input("Horas aulas do professor 2: "))
p2_vh = float(input("Valor da hora aula do professor 2: "))
salario_p1 = p1_h * p1_vh
salario_p2 = p2_h * p2_vh
if salario_p1 > salario_p2:
    print("O salario do professor 1 é de",salario_p1, "\
que é maior que do professor 2, cujo o salario é de,",salario_p2)
else:
    print("O salario do professor 2 é de",salario_p2,"\
que é maior que do professor 1, cujo o salario é de,",salario_p1)
