
# desafio033.py
# Simula aprovação de empréstimo para compra de casa
casa = float(input('Qual o valor da casa? '))  # Lê valor da casa
salario = float(input('Qual o salario do comprador? '))  # Lê salário
anos = int(input('Em quantos anos ele vai pagar a casa? '))  # Lê anos para pagar

# Calcula valor da prestação e limite permitido
prestacao = casa / (anos * 12)
minimo = salario * 0.3

# Exibe informações do financiamento
print('Para pagar a casa de R${:.2f} em {} anos' .format(casa, anos))
print('A prestação será de R${:.2f}' .format(prestacao))

# Verifica se o empréstimo pode ser aprovado
if prestacao <= minimo:
    print('Emprestimo Aprovado! Prestação dentro do limite')
else:
    print('Emprestimo negado! Prestação muito alta')