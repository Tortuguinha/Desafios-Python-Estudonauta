
# desafio035.py
# Solicita dois números e compara qual é maior ou se são iguais
num1 = float(input('Digite o primeiro numero a ser conparado: '))  # Lê o primeiro número
num2 = float(input('Digite o segundo nuemro a ser comparado: '))   # Lê o segundo número

# Compara os números
if num1 > num2:
    print('O primeiro numero é maior!')
elif num2 > num1:
    print('O segundo numero é maior!')
else:
    print('Os numeros são iguais!')