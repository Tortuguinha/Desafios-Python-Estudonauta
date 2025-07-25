# Início das variáveis
soma = 0
quantidade = 0
maior = None
menor = None

continuar = 'S'

while continuar == 'S':
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    quantidade += 1

    # Atualiza o maior e menor valor
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Opção inválida! Digite [S] para continuar ou [N] para parar: ').strip().upper()

# Cálculo da média
media = soma / quantidade if quantidade > 0 else 0

# Resultados finais
print('\n===== RESULTADO FINAL =====')
print(f'Você digitou {quantidade} números.')
print(f'A média dos valores é {media:.2f}')
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')
