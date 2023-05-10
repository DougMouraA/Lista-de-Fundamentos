n1 = float(input("primeiro valor: "))
n2 = float(input("segundo valor: "))
op = input("operacao: ")
r = 0
op = op.lower()
if op == "+" or op == "soma":
    r = n1 + n2
    print("resultado =", r)
elif op == "-" or op == "subtracao":
    r = n1 - n2
    print("resultado =", r)
elif op == "x" or op == "*" or op == "." or op == "multiplicacao":
    r = n1 * n2
    print("resultado =", r)
elif op == "/" or op == "divisao":
    if n2 == 0:
        print("nao e possivel dividir por zero")
    else:
        r = n1 / n2
        print("resultado =", r)
else:
    print ("insira uma operacao valida!")

