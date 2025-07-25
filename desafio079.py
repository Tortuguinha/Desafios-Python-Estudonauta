
# desafio079.py
# Lê vários números, armazena em uma lista e separa em pares e ímpares

# Cria listas para armazenar todos os números, pares e ímpares
numeros = []
pares = []
impares = []

# Loop para ler os números do usuário
while True:
    try:
        # Solicita um número ao usuário
        valor = int(input('Digite um número (ou digite "sair" para encerrar): '))
        # Adiciona o número à lista principal
        numeros.append(valor)
        # Se o número for par, adiciona à lista de pares
        if valor % 2 == 0:
            pares.append(valor)
        else:
            # Se for ímpar, adiciona à lista de ímpares
            impares.append(valor)
    except ValueError:
        # Se o usuário digitar algo que não seja número, encerra o loop
        break

# Mostra o conteúdo das três listas
print(f"\nLista completa: {numeros}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")
