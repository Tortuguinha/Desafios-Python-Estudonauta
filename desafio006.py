
# desafio006.py
# Solicita uma distância em metros e mostra em várias unidades
m = float(input('Digite a distancia em metros: '))  # Lê a distância em metros

# Converte para outras unidades
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
# Exibe as conversões
print('A medida de {} corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm' .format(m, km, hm, dam, dm, cm, mm))