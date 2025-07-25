
# desafio016.py
# Solicita um ângulo e mostra seno, cosseno e tangente
import math
angulo = float(input('digite o angulo que voce deseja calcular: '))  # Lê o ângulo
seno = math.sin(math.radians(angulo))      # Calcula o seno
cosseno = math.cos(math.radians(angulo))   # Calcula o cosseno
tangente = math.tan(math.radians(angulo))  # Calcula a tangente

# Exibe os resultados
print('O angulo de {} tem o SENO de {:.2f}º' .format(angulo, seno))
print('O angulo de {} tem o COSSENO de {:.2f}º' .format(angulo, cosseno))
print('O angulo de {} tem a TANGENTE de {:.2f}º' .format(angulo, tangente))