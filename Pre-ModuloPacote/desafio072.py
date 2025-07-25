# Lê quatro números e guarda numa tupla
numeros = tuple(int(input(f"Digite o {i+1}º número: ")) for i in range(4))

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"\nNúmeros digitados: {numeros}")
print(f"Números pares: {pares if pares else 'Nenhum número par'}")
print(f"Números ímpares: {impares if impares else 'Nenhum número ímpar'}")