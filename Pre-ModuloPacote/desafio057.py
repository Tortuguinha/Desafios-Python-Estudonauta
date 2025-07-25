
# desafio057.py
# Calculadora com menu de operações
num1 = float(input('Primeiro valor: '))  # Lê o primeiro número
num2 = float(input('Segundo valor: '))   # Lê o segundo número

while True:
    # Exibe o menu de opções
    c = int(input('\n[1] Somar\n'
                  '[2] Subtrair\n'
                  '[3] Multiplicar\n'
                  '[4] Dividir\n'
                  '[5] Resto\n'
                  '[6] Exponenciação\n'
                  '[7] Sair do programa\n'
                  'Escolha uma opção: '))

    # Realiza a operação escolhida
    if c == 1:
        print(f'O resultado da soma é {num1 + num2}')
    elif c == 2:
        print(f'O resultado da subtração é {num1 - num2}')
    elif c == 3:
        print(f'O resultado da multiplicação é {num1 * num2}')
    elif c == 4:
        if num2 != 0:
            print(f'O resultado da divisão é {num1 / num2}')
        else:
            print('Erro: divisão por zero!')
    elif c == 5:
        print(f'O resto da divisão é {num1 % num2}')
    elif c == 6:
        print(f'O resultado da exponenciação é {num1 ** num2}')
    elif c == 7:
        print('Você saiu do programa.')
        break
    else:
        print('Opção inválida.')

    # Pergunta se deseja continuar
    continuar = input('\nDeseja realizar outra operação? [S/N]: ').strip().upper()
    if continuar != 'S':
        break
        print('Programa encerrado. Até logo!')
        break

    # Se continuar, pergunta se quer trocar os números
    trocar = input('Deseja trocar os números? [S/N]: ').strip().upper()
    if trocar == 'S':
        num1 = float(input('Novo primeiro valor: '))
        num2 = float(input('Novo segundo valor: '))