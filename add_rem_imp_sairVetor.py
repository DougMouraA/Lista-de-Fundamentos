vet = []
num = 0
opcao = input("Digite A para adicionar um elemnto, R para remover, I \
para imprimir e F para sair: ")
opcao = opcao.upper()
while opcao != "F":
    if opcao == "A":
        vet.append(num)
        num = int(input("Digite o valor para adicionar"))
    elif opcao == "R":
        vet.pop()
    elif opcao == "I":
        print(vet)
    else:
        print("Opcao invalida!")
    opcao = input("Digite A para adicionar um elemnto, R para remover, I \
para imprimir e F para sair: ") 
    opcao = opcao.upper()
