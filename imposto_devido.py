s = float(input("Seu saldo bancario: "))
imp = 0
if s < 100:
    print("Isento de imposto")
elif s < 1000:
    imp = s * 0.01
    print("ISS de 1% e o valor devido e de", imp)
elif s < 10000:
    imp = s * 0.02
    print("ISS de 2% e o valor devido e de", imp)
elif s < 100000:
    imp = s * 0.03
    print("ISS de 3% e o valor devido e de", imp)
else:
    imp = s * 0.05
    print("ISS de 5% e o valor devido e de", imp)
