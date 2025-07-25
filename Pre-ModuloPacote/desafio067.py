# Inicialização das variáveis
total = 0
nome_mais_caro = ''
preco_mais_caro = 0
nome_mais_barato = ''
preco_mais_barato = None  # inicia indefinido até o primeiro produto

continuar = 'S'

while continuar == 'S':
    print('\n=== CADASTRO DE PRODUTO ===')
    nome = input('Nome do produto: ').strip()
    preco = float(input('Preço do produto: R$ '))

    total += preco

    # Verifica produto mais barato
    if preco_mais_barato is None or preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = nome

    # Verifica produto mais caro
    if preco > preco_mais_caro:
        preco_mais_caro = preco
        nome_mais_caro = nome

    continuar = input('Deseja cadastrar outro produto? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Opção inválida. Deseja cadastrar outro produto? [S/N]: ').strip().upper()

# Resultados finais
print('\n=== RESUMO DA COMPRA ===')
print(f'📦 Total gasto: R$ {total:.2f}')
print(f'💸 Produto mais barato: {nome_mais_barato} - R$ {preco_mais_barato:.2f}')
print(f'💰 Produto mais caro: {nome_mais_caro} - R$ {preco_mais_caro:.2f}')
