resp = input("Esta satisfeito (S ou N)? ")
count_s = 0
count_n = 0
p = 0
while resp != "F":
    if resp == "S":
        count_s +=1
    else:
        count_n +=1
    p +=1
    resp = input("Esta satisfeito (S ou N)? ")
if p > 0:
    porcen_s = (count_s / p) * 100
    porcen_n = (count_n / p) * 100
    print("A porcentagem dos que disseram sim e de",porcen_s,"%")
    print("A porcentagem dos que disseram nao e de",porcen_n,"%")
