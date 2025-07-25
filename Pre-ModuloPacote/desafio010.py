
# desafio010.py
# Solicita o preço do produto e o desconto, calcula e mostra o preço final
preco = float(input('Qual o preço do produto? R$'))      # Lê o preço do produto
desconto = int(input('Quanto de desconto ele tem? %'))   # Lê o desconto em porcentagem

# Calcula o fator de desconto
calc = 1 - (desconto / 100)

# Exibe o preço final com desconto
print('O produto que custava R${} com o desconto de {}% passou a custar R${}!' .format(preco, desconto, preco * calc))