# Inicialização de variáveis
total_homens = total_mulheres = 0
maior_idade_homens = maior_idade_mulheres = 0
menor_idade_homens = menor_idade_mulheres = 0

continuar = 'S'

while continuar == 'S':
    print('\n===== NOVO CADASTRO =====')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Valor inválido. Informe o sexo [M/F]: ').strip().upper()

    # Contabiliza sexo
    if sexo == 'M':
        total_homens += 1
        if idade >= 18:
            maior_idade_homens += 1
        else:
            menor_idade_homens += 1
    else:
        total_mulheres += 1
        if idade >= 18:
            maior_idade_mulheres += 1
        else:
            menor_idade_mulheres += 1

    # Deseja continuar?
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Valor inválido. Digite [S] para continuar ou [N] para sair: ').strip().upper()

# Resultados finais
print('\n===== RESUMO DOS DADOS =====')
print(f'Homens cadastrados: {total_homens}')
print(f'- Maiores de 18 anos: {maior_idade_homens}')
print(f'- Menores de 18 anos: {menor_idade_homens}')
print(f'Mulheres cadastradas: {total_mulheres}')
print(f'- Maiores de 18 anos: {maior_idade_mulheres}')
print(f'- Menores de 18 anos: {menor_idade_mulheres}')
