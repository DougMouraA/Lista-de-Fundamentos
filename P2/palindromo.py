def palindromo(f):
    p = False
    for i in range(0, len(f)//2):
        if f[i] == f[len(f) - i - 1]:
            p = True
    if not p:
        return False
    else:
        return True

f = input("Digite algo: ")
if not palindromo:
    print("Nao e um palindromo")
else:
    print("E um palindromo")

