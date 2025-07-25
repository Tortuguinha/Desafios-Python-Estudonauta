valores = []

# Lê 5 valores e armazena na lista
for i in range(5):
    num = int(input(f"Digite o {i+1}º valor: "))
    valores.append(num)

# Encontra o maior e o menor valor
maior = max(valores)
menor = min(valores)

# Mostra os valores digitados
print("\nValores digitados:", valores)

# Mostra o maior valor e suas posições
print(f"\nMaior valor: {maior} nas posições: ", end="")
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i} ", end="")

# Mostra o menor valor e suas posições
print(f"\nMenor valor: {menor} nas posições: ", end="")
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i} ", end="")
