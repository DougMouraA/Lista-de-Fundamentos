s1 = input("Digite a primeira cadeia: ")
s2 = input("Digite a segunda cadeia: ")
for i in range(0, len(s1)):
    for j in range(0, len(s2)):
        if s1[i] == s2[j]:
            print(s1[i])
