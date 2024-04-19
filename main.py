import sys
from figura import Figura

if __name__ == '__main__':
    pontos = sys.argv                               # Lista de argumentos passados na linha de comando
    pontos = pontos[1:]                             # Remove o primeiro argumento, que é o nome do arquivo
    pontos = [float(ponto) for ponto in pontos]     # Converte os argumentos para float

    if len(pontos) % 2 != 0:
        print('A quantidade de argumentos deve ser par')
        sys.exit(1)
    elif len(pontos) < 6:
        print('A quantidade de argumentos deve ser maior ou igual a 6')
        sys.exit(1)

    # Cria uma matriz com os pontos
    matriz = [pontos[i:i+2] for i in range(0, len(pontos), 2)]
    figura = Figura(matriz)                         # Instancia a classe Figura

    print(figura)                                   # Imprime os vértices e lados da figura
    figura.run()                                    # Desenha a figura na tela