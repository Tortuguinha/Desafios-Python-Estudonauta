pessoas = []

while True:
    pessoa = {}
    pessoa['nome'] = input("Nome: ").strip().title()

    # Entrada válida para sexo
    while True:
        sexo = input("Sexo [M/F]: ").strip().upper()
        if sexo in ('M', 'F'):
            pessoa['sexo'] = sexo
            break
        print("Erro! Por favor, digite 'M' para masculino ou 'F' para feminino.")

    pessoa['idade'] = int(input("Idade: "))

    pessoas.append(pessoa)

    continuar = input("Deseja cadastrar outra pessoa? [S/N]: ").strip().upper()
    if continuar != 'S':
        break

# a) Quantidade de pessoas cadastradas
total_pessoas = len(pessoas)

# b) Média, menor e maior idade
idades = [p['idade'] for p in pessoas]
media_idade = sum(idades) / total_pessoas if total_pessoas > 0 else 0
menor_idade = min(idades) if total_pessoas > 0 else 0
maior_idade = max(idades) if total_pessoas > 0 else 0

# c) Listas de mulheres e homens
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
homens = [p['nome'] for p in pessoas if p['sexo'] == 'M']

# d) Listas com idades acima e abaixo da média
acima_media = [p['nome'] for p in pessoas if p['idade'] > media_idade]
abaixo_media = [p['nome'] for p in pessoas if p['idade'] < media_idade]

# Exibindo resultados
print("\n--- RESULTADOS ---")
print(f"a) Total de pessoas cadastradas: {total_pessoas}")
print(f"b) Média de idade: {media_idade:.2f}")
print(f"   Menor idade: {menor_idade}")
print(f"   Maior idade: {maior_idade}")
print(f"c) Mulheres cadastradas: {mulheres}")
print(f"   Homens cadastrados: {homens}")
print(f"d) Pessoas com idade acima da média: {acima_media}")
print(f"   Pessoas com idade abaixo da média: {abaixo_media}")
