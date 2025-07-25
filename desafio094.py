import random
from time import sleep

# Lista principal
numeros = []

def sorteia():
    print("Sorteando 5 números para a lista: ", end='')
    for _ in range(5):
        n = random.randint(1, 100)
        numeros.append(n)
        print(f"{n} ", end='', flush=True)
        sleep(0.3)
    print("\nSorteio concluído.")

def somarPar():
    soma_par = sum(n for n in numeros if n % 2 == 0)
    soma_impar = sum(n for n in numeros if n % 2 != 0)
    print(f"Soma dos valores pares: {soma_par}")
    print(f"Soma dos valores ímpares: {soma_impar}")

# Execução
sorteia()
somarPar()
