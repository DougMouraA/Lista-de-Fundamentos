f = int(input("Numero de funcionarios: "))
s = float(input("Valor do salario minimo vigente: R$ "))
v = float(input("Valor das vendad do mes: R$ "))
c = v*0.05
c_pf = c / f
salario_pf = (s*2) + c_pf
print(c_pf)
print("O salario de cada funcionario e de R$",salario_pf)
