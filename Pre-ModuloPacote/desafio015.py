
# desafio015.py
# Solicita os comprimentos dos catetos e calcula a hipotenusa
import math

catOposto = float(input('Digite o comprimento em CM do cateto oposto: '))      # Lê o cateto oposto
catAdjascente = float(input('Digite o comprimento em CM do cateto adjascente: ')) # Lê o cateto adjascente

# Calcula a hipotenusa usando o teorema de Pitágoras
hipotenusa = math.pow(catOposto, 2) + math.pow(catAdjascente, 2)

# Exibe o comprimento da hipotenusa
print('O comprimento da hipotenusa com catetos dará {:.2f}CM!' .format(math.sqrt(hipotenusa)))