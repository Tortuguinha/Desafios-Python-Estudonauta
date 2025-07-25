
# desafio019.py
# Solicita o nome completo e mostra várias informações sobre ele
nome = str(input('Digite seu nome completo: ')).strip()  # Lê o nome completo
print('Analisando seu nome...')
# Exibe o nome em maiúsculas
print('Seu nome em maiusculas é {}' .format(nome.upper()))
# Exibe o nome em minúsculas
print('Seu nome em minusculas é {}' .format(nome.lower()))
# Exibe o total de letras (sem espaços)
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
# Exibe o tamanho do primeiro nome
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))