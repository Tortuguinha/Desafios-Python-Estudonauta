
# desafio051.py
# Verifica se uma frase é palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()  # Lê a frase
palavras = frase.split()  # Separa em palavras
junto = ''.join((palavras))  # Junta tudo sem espaços
inverso = ''
for letra in range(len(junto) -1, -1, -1):  # Inverte a frase
    inverso += junto[letra]
# Exibe o inverso
print(f'O inverso de {frase} é {inverso}')
# Verifica se é palíndromo
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palindromo')