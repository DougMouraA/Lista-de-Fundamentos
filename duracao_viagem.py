s_h = int(input("Hora da saida: "))
s_m = int(input("Minuto da saida: "))
s_s = int(input("Segundo da saida: "))
c_h = int(input("Hora da chegada: "))
c_m = int(input("Minuto da chegada: "))
c_s = int(input("Segundo da chegada: "))
dif_h = c_h - s_h
dif_m = c_m - s_m
dif_s = c_s - s_s
print("A viagem durou,",dif_h,"horas,",dif_m,"minutos e",dif_s,"segundos.")
