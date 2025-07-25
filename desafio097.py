def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    
    Parâmetros:
    n (int): Número a ser calculado o fatorial.
    show (bool): Se True, mostra o processo de cálculo. Se False, mostra só o resultado.

    Retorna:
    int: O fatorial de n.
    """
    resultado = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end=' ')
            print('x' if i > 1 else '=', end=' ')
        resultado *= i
    print(resultado if show else '', end='\n' if show else '')
    return resultado

# Programa principal com repetição
while True:
    num = int(input("\nDigite um número para calcular o fatorial: "))
    mostrar = input("Deseja mostrar o processo? [S/N]: ").strip().upper() == 'S'

    print(f"\nResultado: {fatorial(num, show=mostrar)}")

    continuar = input("\nDeseja calcular o fatorial de outro número? [S/N]: ").strip().upper()
    if continuar != 'S':
        print("\nEncerrando o programa. Até logo!")
        break
