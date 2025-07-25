
# desafio045.py
# Soma todos os valores ímpares múltiplos de 3 entre 1 e 500
soma = 0
cont = 0
for a in range (1, 501, 2):  # Percorre apenas ímpares
    if a % 3 == 0:
        cont = cont + 1
        soma = soma + a
# Exibe o resultado
print(f'A soma de todos os {cont} valores solicitados é {soma}')