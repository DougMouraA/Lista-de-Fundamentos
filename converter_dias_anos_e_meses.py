d = int(input("dias: "))
ano = 0
mes = 0
dia = 0
dias = d
if d < 0:
    print("Valor invalido")
else:
    if d >= 365:
        ano = d // 365
        d = d % 365
    if d >= 30:
        mes = d // 30
        d = d % 30
    if d <= 29:
        dia = d
    print(dias,"dias resulta em",ano,"anos,",mes,"meses e", dia,"dias.")

