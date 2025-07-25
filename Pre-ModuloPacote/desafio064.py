print('TABUADA INTERATIVA 📊')
print('Digite um número para ver sua tabuada.')
print('Digite um número negativo para encerrar.\n')

numero = 0  # inicialização

while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    print(f'--- Tabuada de {numero} ---')
    multiplicador = 1
    while multiplicador <= 10:
        resultado = numero * multiplicador
        print(f'{numero} x {multiplicador} = {resultado}')
        multiplicador += 1
    print('-------------------------\n')

print('Programa encerrado. Até logo 👋')
