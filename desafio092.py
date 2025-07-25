def escreva(texto):
    tamanho = len(texto) + 4
    print("~" * tamanho)
    print(f"  {texto}")
    print("~" * tamanho)

# Programa principal
escreva("Olá, mundo!")
escreva("Curso de Python")
escreva("Função personalizada")
