
# desafio053.py
# Encontra o maior e o menor peso entre 5 pessoas
pesado = 0
leve = 100

# Loop para ler o peso de 5 pessoas
for c in range (1, 6):
    contador = float(input(f'Peso(kg) da {c}ª pessoa: '))
    if contador > pesado:
        pesado = contador  # Atualiza o maior peso
    if contador < leve:
        leve = contador    # Atualiza o menor peso
# Exibe os resultados
print(f'O maior peso registrado foi de {pesado}KG')
print(f'O menor peso registrado foi de {leve}KG')