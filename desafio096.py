from datetime import date

def voto(ano_nascimento):
    """Retorna a situação do voto de acordo com o ano de nascimento."""
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO"
    elif 16 <= idade < 18 or idade > 70:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"

# Programa principal
nasc = int(input("Digite o ano de nascimento: "))
print(voto(nasc))
