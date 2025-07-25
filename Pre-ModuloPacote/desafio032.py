
# desafio032.py
# Solicita os lados de um triângulo e verifica se é possível formar um triângulo
ladoa = int(input('Digite o lado A do triangulo: '))  # Lê lado A
ladob = int(input('Digite o lado B do trnagulo: '))   # Lê lado B
ladoc = int(input('Digite o lado C do triangulo: '))  # Lê lado C

# Calcula as somas para verificar a existência do triângulo
soma1 = ladoc + ladoa
soma2 = ladoc + ladob
soma3 = ladoa + ladob

# Verifica se os lados formam um triângulo
if ladoc < soma3 and ladob < soma1 and ladoa < soma2:
    print('Otimo os lados fazem um triangulo!')
else:
    print('Que pena, os lados não fazem um triangulo!')