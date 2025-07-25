from time import sleep

def contador(inicio, fim, passo):
    print("-=" * 20)
    print(f"Contando de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:")
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont} ", end='', flush=True)
            sleep(0.3)
            cont += abs(passo)
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end='', flush=True)
            sleep(0.3)
            cont -= abs(passo)
    print("FIM!")
    print("-=" * 20)

# Contagens solicitadas
contador(0, 10, 1)
contador(10, 0, 2)

# Contagem personalizada
print("Agora é a sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))
contador(ini, fim, pas)
