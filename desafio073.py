produtos = (
    "Arroz", 15.90,
    "Feijão", 8.50,
    "Macarrão", 5.75,
    "Óleo", 7.20,
    "Açúcar", 4.30
)

print(f"{'Produto':<15} {'Preço (R$)':>10}")
print("-" * 26)

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f"{nome:<15} {preco:>10.2f}")
print("-" * 26)
