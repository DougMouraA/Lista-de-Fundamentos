d = int(input("Dinheiro: "))
n = 0
while d > 0:
    qtd50 = 0
    qtd20 = 0
    qtd10 = 0
    qtd5 = 0
    qtd1 = 0
    n = d
    if n >= 50:
        qtd50 = n // 50
        n = n % 50
    if n >= 20:
        qtd20 = n // 20
        n = n % 20
    if n >= 10:
        qtd10 = n // 10
        n = n % 10
    if n >= 5:
        qtd5 = n // 5
        n = n % 5
    if n >= 1:
        qtd1 = n // 1
    print(d,"=",qtd50,"de 50,",qtd20,"de 20,",qtd10,"de 10,",qtd5,"de 5 e\
",qtd1,"de 1,")
    d = int(input("Dinheiro: "))


    
