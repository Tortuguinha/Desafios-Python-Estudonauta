def leiaInt(msg):
    while True:
        valor = input(msg).strip()
        if valor.isdigit() or (valor.startswith('-') and valor[1:].isdigit()):
            return int(valor)
        else:
            print(f"\033[31mERRO! Digite um número inteiro válido.\033[m")

# Exemplo de uso
n = leiaInt("Digite um número inteiro: ")
print(f"Você digitou o número {n}.")
