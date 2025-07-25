palavras = ("casa", "computador", "arvore", "python", "programacao", "mesa")

vogais = "aeiou"

for palavra in palavras:
    lista_vogais = []
    for letra in palavra:
        if letra in vogais:
            lista_vogais.append(letra)
    print(f"Na palavra '{palavra}' temos as vogais: {', '.join(lista_vogais)}")
