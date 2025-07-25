# desafio058.py
# Solicita uma frase ao usuário e verifica se é um palíndromo
frase = input('Digite uma frase: ').strip().upper()  # Lê a frase e converte para maiúsculas

# Remove espaços da frase para considerar apenas as letras
frase_sem_espaco = frase.replace(' ', '')

# Verifica se a frase sem espaços é igual ao seu reverso
if frase_sem_espaco == frase_sem_espaco[::-1]:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo.')
num = int(input('Digite o número para calcular o fatorial: '))
resultado = 1
contador = num

while contador > 1:
    resultado *= contador
    contador -= 1

print(f'{num}! = {resultado}')
