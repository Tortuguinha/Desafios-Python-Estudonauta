def ajuda(comando):
    """
    Exibe a ajuda interativa do Python para o comando informado.
    """
    titulo(f"Acessando o manual do comando '{comando}'", cor=4)
    print('\033[7m')  # Fundo branco, texto preto
    help(comando)
    print('\033[m')  # Reset


def titulo(msg, cor=0):
    """
    Exibe um título formatado com cores.

    Cores disponíveis:
    0 - Branco
    1 - Vermelho
    2 - Verde
    3 - Amarelo
    4 - Azul
    5 - Roxo
    6 - Ciano
    7 - Cinza
    """
    cores = [
        '\033[m',        # 0 - Sem cor
        '\033[1;31m',    # 1 - Vermelho
        '\033[1;32m',    # 2 - Verde
        '\033[1;33m',    # 3 - Amarelo
        '\033[1;34m',    # 4 - Azul
        '\033[1;35m',    # 5 - Roxo
        '\033[1;36m',    # 6 - Ciano
        '\033[1;37m',    # 7 - Branco/Cinza
    ]
    tam = len(msg) + 4
    print(cores[cor] + '─' * tam)
    print(f'  {msg}')
    print('─' * tam + '\033[m')


# Programa principal
while True:
    titulo("SISTEMA DE AJUDA PYTHON", cor=2)
    comando = input("Função ou biblioteca ('FIM' para sair): ").strip()
    if comando.upper() == 'FIM':
        titulo("Até logo!", cor=1)
        break
    else:
        ajuda(comando)