# desafio034.py
# Solicita um número inteiro e converte para binário, octal ou hexadecimal
num = int(input('Digite um numero inteiro a ser convertido: '))  # Lê o número

# Exibe opções de conversão
print('Escolha uma das bases para converter:\n'
      '[1] Converter para Binário\n'
      '[2] Converter para Octal\n'
      '[3] Converter para Hexadecimal')

opcao = int(input('Digite a opção: '))  # Lê a opção

# Realiza a conversão conforme a escolha
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}' .format(num, bin(num)))
elif opcao == 2:
    print('{} convertido em OCTAL é igual a {}' .format(num, oct(num)))
else:
    print('{} convertido para HEXADECIAML é igual a {}' .format(num, hex(num)))