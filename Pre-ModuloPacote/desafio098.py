def ficha(nome='<desconhecido>', gols=0):
    try:
        gols = int(gols)
    except:
        gols = 0
    return {'Nome': nome, 'Gols': gols}

# Lista para armazenar várias fichas
elenco = []

# Coletando dados dos jogadores
while True:
    nome = input("Nome do jogador (ou ENTER para parar): ").strip()
    gols = input("Número de gols: ").strip()
    jogador = ficha(nome if nome else '<desconhecido>', gols)
    elenco.append(jogador)

    cont = input("Deseja adicionar outro jogador? [S/N] ").strip().upper()
    if cont != 'S':
        break

# Exibindo todos os jogadores em tabela
print("\n--- FICHA DOS JOGADORES ---")
print(f"{'Nome':<20}{'Gols':<5}")
print("-" * 25)
for j in elenco:
    print(f"{j['Nome']:<20}{j['Gols']:<5}")
print("-" * 25)
