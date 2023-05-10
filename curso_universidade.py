maior = 0
mCodigo = 0
codigo = int(input("Digite o codigo do curso: "))
while codigo > 0:
    nvagas = int(input("Numero de vagas: "))
    ncandm = int(input("Numero de candidatos do sexo masculinos: "))
    ncandf = int(input("Numero de candidatos do sexo femininos: "))
    total = ncandm + ncandf
    candVag = total / nvagas
    if candVag > maior:
        maior = candVag
        mCodigo = codigo
    femCandp = (ncandf / total)*100
    print("O numero de candidatos por vagas do curso", codigo,"e de",candVag)
    print("A porcentagem de candidatos do sexo feminino no curso", codigo," e de",\
          femCandp,"%")
    codigo = int(input("Digite o codigo do curso: "))
if maior > 0:
    print("O curso com maior candidato/vaga e o",mCodigo,"Com",maior,"candidato/vaga")
    
