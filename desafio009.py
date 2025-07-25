
# desafio009.py
# Solicita largura e altura da parede, calcula área e quantidade de tinta
largura = float(input('Digite a largura da parede: '))  # Lê a largura
altura = float(input('Digite a altura da parede: '))    # Lê a altura

# Calcula a área da parede
area = largura * altura

# Exibe área e quantidade de tinta necessária (2L por m²)
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².' .format(largura, altura, area))
print('Para pintar sua parede, você irá precisar de {:.2f}L de tinta' . format(area * 2))