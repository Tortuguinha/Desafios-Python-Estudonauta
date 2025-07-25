numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

while True:
    try:
        num = int(input("Digite um número entre 0 e 20: "))
        if 0 <= num <= 20:
            print(f"O número {num} por extenso é: {numeros_por_extenso[num]}")
            break  # Sai do loop quando o valor for válido
        else:
            print("Número inválido! Por favor, digite um número entre 0 e 20.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
