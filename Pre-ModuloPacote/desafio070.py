# Tupla com os 20 primeiros colocados na ordem da tabela
times = (
    "Palmeiras", "Corinthians", "Fluminense", "Athletico-PR", "Atlético-MG",
    "Flamengo", "Botafogo", "Bragantino", "América-MG", "São Paulo",
    "Fortaleza", "Internacional", "Cruzeiro", "Santos", "Vasco",
    "Goiás", "Coritiba", "Bahia", "Atlético-GO", "Grêmio"
)

# a) 5 primeiros colocados
print("5 primeiros colocados:")
for time in times[:5]:
    print(time)

# b) 4 últimos colocados
print("\n4 últimos colocados:")
for time in times[-4:]:
    print(time)

# c) times em ordem alfabética
print("\nTimes em ordem alfabética:")
for time in sorted(times):
    print(time)

# d) time do meio
# Como são 20 times, o "do meio" pode ser o 10º e o 11º (índices 9 e 10)
meio1 = times[9]
meio2 = times[10]
print(f"\nTimes do meio da tabela: {meio1} e {meio2}")
