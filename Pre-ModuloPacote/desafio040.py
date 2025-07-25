
# desafio040.py
# Calcula o IMC e informa se está dentro da faixa ideal conforme idade e sexo
idade = int(input('Digite sua idade: '))  # Lê idade
sexo = input('Digite seu sexo (M para homem ou F para mulher): ').strip().upper()  # Lê sexo
peso = float(input('Digite seu peso (kg): '))  # Lê peso
altura = float(input('Digite sua altura (m): '))  # Lê altura

imc = peso / (altura ** 2)  # Calcula IMC
print(f'\nSeu IMC é {imc:.2f}\n')

# Verificação por idade e sexo
if idade <= 12:
    faixa = 'criança'
    imc_min, imc_max = 14, 17
    status = 'dentro' if imc_min <= imc <= imc_max else 'fora'
    print(f'Como {faixa}, você está {status} da faixa ideal para crianças.')
    print(f'O IMC ideal para essa faixa é entre {imc_min} e {imc_max}.')
elif idade <= 17:
    faixa = 'adolescente'
    if sexo == 'M':
        imc_min, imc_max = 18, 24
    else:
        imc_min, imc_max = 17, 23
    status = 'dentro' if imc_min <= imc <= imc_max else 'fora'
    print(f'Como {faixa} do sexo {"masculino" if sexo == "M" else "feminino"}, você está {status} da faixa ideal para adolescentes.')
    print(f'O IMC ideal para essa faixa é entre {imc_min} e {imc_max}.')
elif idade < 60:
    faixa = 'adulto'
    if sexo == 'M':
        imc_min, imc_max = 20, 25
    else:
        imc_min, imc_max = 18.5, 24.9
    status = 'dentro' if imc_min <= imc <= imc_max else 'fora'
    print(f'Como {faixa} do sexo {"masculino" if sexo == "M" else "feminino"}, você está {status} da faixa ideal para adultos.')
    print(f'O IMC ideal para essa faixa é entre {imc_min} e {imc_max}.')
else:
    faixa = 'idoso'
    if sexo == 'M':
        imc_min, imc_max = 22, 27
    else:
        imc_min, imc_max = 21, 26
    status = 'dentro' if imc_min <= imc <= imc_max else 'fora'
    print(f'Como {faixa} do sexo {"masculino" if sexo == "M" else "feminino"}, você está {status} da faixa ideal para idosos.')
    print(f'O IMC ideal para essa faixa é entre {imc_min} e {imc_max}.')
