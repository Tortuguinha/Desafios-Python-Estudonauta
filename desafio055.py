
# desafio055.py
# Solicita o sexo do usuário e valida a entrada
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()  # Lê o sexo

# Loop de validação
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo: ')).strip().upper()
# Exibe confirmação
print(f'Sexo {sexo} registrado com sucesso')