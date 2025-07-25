
# desafio026.py
# Solicita a velocidade do carro e calcula multa se necessário
vel = int(input('Digite a velocidade atual do carro: '))  # Lê a velocidade
multa = (vel - 80) * 7  # Calcula o valor da multa

# Verifica se está acima do limite
if vel <= 80:
    print('Parabens, continue dirigindo com segurança!')
else:
    print('Diminui a velocidade para não causar acidentes!')
    print('Voce tambem foi multado em R${}' .format(multa))