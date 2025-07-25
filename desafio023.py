
# desafio023.py
# Solicita uma frase e analisa ocorrências da letra 'A'
frase = str(input('digite uma frase: ')).strip().upper()  # Lê a frase
# Conta quantas vezes 'A' aparece
print('A letra A aparece {} vezes na frase.' .format(frase.count('A')))
# Mostra a posição da primeira ocorrência de 'A'
print('A primeira letra A aparece na posição {}.' .format(frase.find('A') + 1))
# Mostra a posição da última ocorrência de 'A'
print('A ultima letra A aparece na posição {}.' .format(frase.rfind('A') + 1))