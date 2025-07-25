
# desafio078.py
# Lê vários números, armazena em uma lista e exibe informações solicitadas

# Cria uma lista para armazenar os números digitados
numeros = []

# Loop para ler os números do usuário
while True:
    try:
        # Solicita um número ao usuário
        valor = int(input('Digite um número (ou digite "sair" para encerrar): '))
        # Adiciona o número à lista
        numeros.append(valor)
    except ValueError:
        # Se o usuário digitar algo que não seja número, encerra o loop
        break

# Mostra quantos números foram digitados
print(f"\nA) Foram digitados {len(numeros)} números.")
# Mostra a lista de valores em ordem decrescente
print(f"B) Lista de valores em ordem decrescente: {sorted(numeros, reverse=True)}")

# Conta quantas vezes o número 5 foi digitado
qtd_5 = numeros.count(5)
if qtd_5 > 0:
    # Se o número 5 foi digitado, mostra quantas vezes e que está na lista
    print(f"C) O valor 5 foi digitado {qtd_5} vezes e está na lista.")
else:
    # Se o número 5 não foi digitado
    print("C) O valor 5 não foi digitado e não está na lista.")
