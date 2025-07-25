from datetime import datetime

pessoas = []

while True:
    dados = {}
    dados['nome'] = input("Nome: ").strip().title()
    ano_nasc = int(input("Ano de nascimento: "))
    dados['idade'] = datetime.now().year - ano_nasc
    dados['ctps'] = int(input("Carteira de trabalho (0 se não tiver): "))

    if dados['ctps'] != 0:
        dados['ano_contratacao'] = int(input("Ano de contratação: "))
        dados['salario'] = float(input("Salário: R$ "))
        anos_contribuicao_restantes = 35 - (datetime.now().year - dados['ano_contratacao'])
        if anos_contribuicao_restantes < 0:
            anos_contribuicao_restantes = 0
        dados['ano_aposentadoria'] = datetime.now().year + anos_contribuicao_restantes

    pessoas.append(dados)

    # Perguntar se deseja continuar
    continuar = input("Deseja cadastrar outra pessoa? [S/N] ").strip().upper()
    if continuar != 'S':
        break

# Exibindo todos os dados cadastrados
print("\n--- DADOS DAS PESSOAS CADASTRADAS ---")
for i, pessoa in enumerate(pessoas, start=1):
    print(f"\nPessoa {i}:")
    for chave, valor in pessoa.items():
        print(f"  {chave.capitalize().replace('_', ' ')}: {valor}")