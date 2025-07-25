
# desafio022.py
# Solicita o nome completo e verifica se contém 'SILVA'
nome = str(input('Qual o seu nome completo: ')).strip()  # Lê o nome completo
# Verifica se 'SILVA' está no nome
print('Seu nome tem Silva? {}' .format('SILVA' in nome.upper()))