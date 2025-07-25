
# desafio028.py
# Solicita a distância da viagem e calcula o preço
viagem = int(input('Digite em quilometros a distancia da viagem: '))  # Lê a distância

# Calcula o preço conforme a distância
if viagem <= 200:
    preco = viagem * 0.5
    print('Sua viagem custou R${}' .format(preco))
else:
    preco = viagem * 0.45
    print('Sua viagem custou R${}' .format(preco))