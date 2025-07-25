print('=' * 30)
print('      BANCO DO TORTUGA 🏦')
print('=' * 30)

valor = int(input('Qual valor você quer sacar? R$ '))
cedula = 100
total = valor

while total > 0:
    notas = total // cedula
    if notas > 0:
        print(f'Total de {notas} cédula(s) de R$ {cedula}')
        total -= notas * cedula

    # Atualiza para a próxima cédula disponível
    if cedula == 100:
        cedula = 50
    elif cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 5
    elif cedula == 5:
        cedula = 2
    else:
        # Caso sobre um valor não representável com as cédulas disponíveis
        if total > 0:
            print(f'⚠️ Não é possível sacar R$ {total} com as cédulas disponíveis.')
        break

print('=' * 30)
print('Volte sempre ao BANCO DO TORTUGA! 🐢💰')
