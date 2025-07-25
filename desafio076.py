valores = []

while True:
    try:
        num = int(input("Digite um valor: "))
        if num not in valores:
            valores.append(num)
            print("Valor adicionado com sucesso!")
        else:
            print("Valor duplicado! Não será adicionado.")
    except ValueError:
        print("Digite apenas números inteiros.")

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar != 'S':
        break

# Exibe a lista ordenada
print("\nValores únicos digitados, em ordem crescente:")
print(sorted(valores))
