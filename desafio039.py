
# desafio039.py
# Solicita lados de um triângulo, verifica se é possível formar e classifica
ladoa = int(input('Digite o lado A do triangulo: '))  # Lê lado A
ladob = int(input('Digite o lado B do trnagulo: '))   # Lê lado B
ladoc = int(input('Digite o lado C do triangulo: '))  # Lê lado C

# Calcula as somas para verificar existência do triângulo
soma1 = ladoc + ladoa
soma2 = ladoc + ladob
soma3 = ladoa + ladob

# Verifica se é possível formar triângulo
if ladoc < soma3 and ladob < soma1 and ladoa < soma2:
    print('Otimo os lados fazem um triangulo!')
    # Classifica o tipo de triângulo
    if ladoa == ladob == ladoc:
        print('O tirangulo é Equilátero!')
    elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
        print('O triangulo é Isóceles')
    else:
        print('O triangulo é Escaleno')
else:
    print('Que pena, os lados não fazem um triangulo!')