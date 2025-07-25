from time import sleep

def cadastro_jogador():
    jogador = {}
    jogador['nome'] = input("Nome do jogador: ").strip().title()
    total_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    gols = []
    for i in range(1, total_partidas + 1):
        gols.append(int(input(f"Quantos gols na partida {i}? ")))

    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    jogador['aproveitamento'] = (jogador['total'] / total_partidas) * 100 if total_partidas > 0 else 0

    return jogador

def mostrar_dados_jogador(jogador):
    print("\n--- DADOS DO JOGADOR ---")
    for chave, valor in jogador.items():
        if chave == 'aproveitamento':
            print(f"Aproveitamento: {valor:.2f}%")
        else:
            print(f"{chave.capitalize()}: {valor}")

    print("\n--- DESEMPENHO POR PARTIDA ---")
    for i, g in enumerate(jogador['gols'], start=1):
        print(f"Na partida {i}, fez {g} gol(s).")

    print(f"\nTotal de gols no campeonato: {jogador['total']}")
    print(f"Aproveitamento de {jogador['nome']}: {jogador['aproveitamento']:.2f}%")

def mostrar_tabela_time(time):
    print("\n--- TABELA DE APROVEITAMENTO DO TIME ---")
    print(f"{'Nome':<15}{'Gols':<20}{'Total':<10}{'Aproveitamento'}")
    print("-" * 60)
    for jogador in time:
        gols_str = ', '.join(str(g) for g in jogador['gols'])
        print(f"{jogador['nome']:<15}{gols_str:<20}{jogador['total']:<10}{jogador['aproveitamento']:.2f}%")
    print("-" * 60)

def main():
    while True:
        escolha = input("\nEscolha a opção:\n1 - Jogador individual\n2 - Time inteiro\n0 - Sair\nSua opção: ").strip()

        if escolha == '1':
            # Jogador individual
            jogador = cadastro_jogador()
            mostrar_dados_jogador(jogador)

            cont = input("\nDeseja ver o aproveitamento de outro jogador? [S/N] ").strip().upper()
            if cont != 'S':
                print("Encerrando o programa. Obrigado!")
                break

        elif escolha == '2':
            # Time inteiro
            time = []
            num_jogadores = int(input("Quantos jogadores tem o time? "))

            for _ in range(num_jogadores):
                print("\nCadastro de um novo jogador:")
                jogador = cadastro_jogador()
                time.append(jogador)
                print("-" * 30)
                sleep(0.5)

            mostrar_tabela_time(time)

            # Totais do time
            total_gols_time = sum(j['total'] for j in time)
            total_partidas_time = sum(len(j['gols']) for j in time)
            aproveitamento_time = (total_gols_time / total_partidas_time) * 100 if total_partidas_time > 0 else 0

            print(f"\nTotal de gols do time: {total_gols_time}")
            print(f"Aproveitamento médio do time: {aproveitamento_time:.2f}%")

            cont = input("\nDeseja fazer outra consulta? [S/N] ").strip().upper()
            if cont != 'S':
                print("Encerrando o programa. Obrigado!")
                break

        elif escolha == '0':
            print("Encerrando o programa. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
