palavra = input("Digite uma palavra: ")
plvrPar = ""
plvrImpar = ""
for i in range (len(palavra)):
    if i % 2 == 0:
        plvrPar += palavra[i]
    else:
        plvrImpar += palavra[i]

print(plvrImpar, plvrPar)
