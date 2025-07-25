
# desafio021.py
# Solicita o nome da cidade e verifica se começa com 'SANTO'
cid = str(input('Em que cidade voce nasceu? ')).strip()  # Lê o nome da cidade
# Verifica se os 5 primeiros caracteres são 'SANTO'
print(cid[:5].upper() == 'SANTO')