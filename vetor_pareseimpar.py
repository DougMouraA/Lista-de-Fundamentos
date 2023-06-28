somapar = 0
somaimpar = 0
elem = []
for i in range(0, 10):
    elem.append(int(input("digite um valor: ")))
    if elem[i] % 2 == 0:
        somapar += elem[i]
    if i % 2 != 0:
        somaimpar += elem[i]
resultado = somapar - somaimpar
print("o resultado:", resultado)
