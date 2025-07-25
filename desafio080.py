
# desafio080.py
# Verifica se os parênteses de uma expressão estão corretamente abertos e fechados

# Loop principal do programa
while True:
    # Solicita uma expressão ao usuário
    expressao = input('Digite uma expressão com parênteses: ')
    pilha = []  # Lista usada como pilha para verificar os parênteses
    # Percorre cada caractere da expressão
    for char in expressao:
        if char == '(':  # Se encontrar um parêntese aberto, adiciona à pilha
            pilha.append(char)
        elif char == ')':  # Se encontrar um parêntese fechado
            if pilha:
                pilha.pop()  # Remove um parêntese aberto correspondente
            else:
                pilha.append(')')  # Se não houver parêntese aberto, marca erro
                break
    # Se a pilha estiver vazia, os parênteses estão corretos
    if not pilha:
        print('Expressão válida!')
        try:
            # Tenta avaliar a expressão
            resultado = eval(expressao)
            print(f'Resultado da expressão: {resultado}')
        except Exception as e:
            # Se não for possível avaliar, mostra o erro
            print(f'Expressão válida, mas não pôde ser avaliada: {e}')
        # Pergunta ao usuário se deseja continuar
        while True:
            continuar = input('Deseja continuar? (S/N): ').strip().lower()
            if continuar in ['s', 'sim', 'ss']:
                break  # Continua o programa
            elif continuar in ['n', 'nao', 'não', 'nn']:
                print('Encerrando o programa.')
                exit()  # Encerra o programa
            else:
                print('Opção inválida! Digite S para continuar ou N para sair.')
    else:
        # Se a pilha não estiver vazia, os parênteses estão incorretos
        print('Expressão inválida! Tente novamente.')