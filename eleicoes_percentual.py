eleitores = int(input("Numero de eleitores: "))
v_b = int(input("Numero de votos brancos: "))
v_n = int(input("Numero de votos nulos: "))
v_v = int(input("Numero de votos validos: "))
p_b = (v_b / eleitores) * 100
p_n = (v_n / eleitores) * 100
p_v = (v_v / eleitores) * 100
print("O percentual de votos validos e de",p_v,"%.")
print("Votos brancos,",p_b,"%","e votos nulos e de",p_n,"%.")
