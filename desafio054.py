
# desafio054.py
# Analisa dados de 4 pessoas: média de idade, mais velho, mais novo, quantidade de homens e mulheres
nome = ''; sexo = ''; nomeVelho = ''; sexoVelho = ''; nomeNovo = ''; sexoNovo = ''
idade = 0; media = 0; maisVelho = 0; contadorF = 0; contadorM = 0; maisVelho = 0; maisNovo = 100

# Loop para ler dados de 4 pessoas
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    # Armazena a pessoa mais velha
    if idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
        sexoVelho = sexo

    # Armazena a pessoa mais nova
    if idade < maisNovo:
        maisNovo = idade
        nomeNovo = nome
        sexoNovo = sexo

    # Contador de mulheres e homens
    if sexo == 'M':
        contadorM += 1
    else:
        contadorF += 1

# cálculo da média de idades
media_idade = media / 4
# Exibe os resultados
print(f'A média de idade do grupo é {media_idade:.1f} anos.')
print(f'A pessoa mais velha é {nomeVelho}, tem {maisVelho} anos e é do sexo {"masculino" if sexoVelho == "M" else "feminino"}.')
print(f'A pessoa mais nova é {nomeNovo}, tem {maisNovo} anos e é do sexo {"masculino" if sexoNovo == "M" else "feminino"}.')
print(f'Ao todo existem {contadorF} mulheres e {contadorM} homens')