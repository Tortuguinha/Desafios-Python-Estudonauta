
# desafio041.py
# Calcula o valor final de uma compra conforme a forma de pagamento
pagamento = float(input('Digite o valor a ser pago: R$'))  # Lê o valor da compra
# Exibe opções de pagamento
print('Selecione a forma de pagamento:\n'
      '[1] À vista dinheiro/cheque \n'
      '[2] À vista no cartão \n'
      '[3] Em 2x no cartão\n'
      '[4] em 3x ou mais no cartão')

opcao = int(input('Qual é a opção? '))  # Lê a opção

# Calcula o valor conforme a opção escolhida
if opcao == 1:
    total = pagamento * 0.90  # 10% de desconto
elif opcao == 2:
    total = pagamento * 0.95  # 5% de desconto
elif opcao == 3:
    total = pagamento
    parcela = pagamento / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
else:
    divisao = int(input('Digite quantas vezes você quer dividir: '))
    total = pagamento * 1.20  # 20% de juros
    parcela = total / divisao
    print(f'Sua compra será parcelada em {divisao}x de R${parcela:.2f}')

# Exibe o valor final
print(f'Sua compra de {pagamento:.2f} vai custar R${total:.2f}')