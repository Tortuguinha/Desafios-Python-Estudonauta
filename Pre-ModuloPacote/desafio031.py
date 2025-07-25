
# desafio031.py
# Solicita o salário e calcula o novo salário com aumento
salario = float(input('Digite o salario do funcionario: '))  # Lê o salário

# Aplica aumento conforme faixa salarial
if salario <= 1250.0:
    novoSalario = salario * 1.15
    print('O novo salario do funcionario será de {:.2f}' .format(novoSalario))
else:
    novoSalario = salario * 1.10
    print('O novo salario do funcionario será de {:.2f}' .format(novoSalario))