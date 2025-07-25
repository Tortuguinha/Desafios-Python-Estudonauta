
# desafio011.py
# Solicita o salário e o aumento, calcula e mostra o novo salário
preco = float(input('Qual o salário do funcionário? R$'))  # Lê o salário
aumento = int(input('Quanto de aumento ele vai ter? %'))   # Lê o aumento em porcentagem

# Calcula o fator de aumento
calc = 1 + (aumento / 100)

# Exibe o novo salário após o aumento
print('O salario do funcionário que era de R${} com o aumento de {}% passou a ser R${}!' .format(preco, aumento, preco * calc))