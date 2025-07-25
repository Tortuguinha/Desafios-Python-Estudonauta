import random

# Gera 5 números aleatórios entre 1 e 100
numeros = tuple(random.randint(1, 100) for _ in range(5))

print("Números gerados:", numeros)
print("Menor valor:", min(numeros))
print("Maior valor:", max(numeros))
print("Soma dos valores:", sum(numeros))
print("Média dos valores:", sum(numeros) / len(numeros))
print("Números em ordem crescente:", sorted(numeros))
print("Números em ordem decrescente:", sorted(numeros, reverse=True))