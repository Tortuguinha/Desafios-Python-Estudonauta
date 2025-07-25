
# desafio002.py
# Solicita uma entrada do usuário e mostra várias informações sobre ela
caixa = input("Digite algo: ")  # Lê uma string do usuário
print(type(caixa))  # Mostra o tipo da variável
print('É um alfabetico? {}' .format(caixa.isalpha()))  # Verifica se é apenas letras
print('É um numero? {}' .format(caixa.isnumeric()))    # Verifica se é apenas números
print('É um alfanumerico? {}' .format(caixa.isalnum())) # Verifica se é letras ou números
print('Está na tabela ASCII? {}' .format(caixa.isascii())) # Verifica se está na tabela ASCII
print('É um numero inteiro? {}' .format(caixa.isdigit())) # Verifica se é dígito
print('É um numero decimal? {}' .format(caixa.isdecimal())) # Verifica se é decimal
print('Pode ser usado como nome de variavel? {}' .format(caixa.isidentifier())) # Verifica se pode ser nome de variável
print('Está em minusculo? {}' .format(caixa.islower())) # Verifica se está em minúsculo
print('É printavel? {}' .format(caixa.isprintable())) # Verifica se é printável
print('É um espaço em branco? {}' .format(caixa.isspace())) # Verifica se é espaço
print('É um titulo? {}' .format(caixa.istitle())) # Verifica se está em formato título
print('Está em maiusculo? {}' .format(caixa.isupper())) # Verifica se está em maiúsculo