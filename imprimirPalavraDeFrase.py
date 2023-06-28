frase = input("Digite uma frase: ")
palavra = ""
for i in range(0, len(frase)):
    if frase[i] != " ":
        palavra += frase[i]
    else:
        if palavra != "":
            print(palavra)
            palavra = ""
if palavra != "":
    print(palavra)
