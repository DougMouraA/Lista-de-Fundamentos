def tempC(c):
    tmp = 0
    for i in range(0, 10):
        tmp = float(input("Digite a temperatura em Celsius: "))
        c[i] = tmp
    return c
    
def converter(c, f):
    for i in range(0, 10):
        f[i] = (c[i]*(9/5)) + 32
    return f

def mediaC(c):
    soma = 0
    for i in range(0, 10):
        soma += c[i]
    media = soma / 10
    return media

def mediaF(f):
    soma = 0
    for i in range(0, 10):
        soma += f[i]
    media = soma / 10
    return media

def qtdMediaF(mediaF, f):
    contF = 0
    for i in range(0, 10):
        if f[i] > mediaF:
            contF += 1
    return contF

c = [0]*10
f = [0]*10
c = tempC(c)
f = converter(c, f)
mediaC = mediaC(c)
mediaF = mediaF(f)
qtdMediaF = qtdMediaF(mediaF, f)
print(mediaC, mediaF, qtdMediaF)
