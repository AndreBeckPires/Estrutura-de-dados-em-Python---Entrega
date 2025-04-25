from collections import deque

VERDE = '\033[92m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'
VERMELHO = '\033[91m'

def ler_mapa(arquivo):
    with open(arquivo, 'r') as f:
        return [list(linha.strip()) for linha in f.readlines()]

def encontrar_posicao(mapa, caractere):
    for y, linha in enumerate(mapa):
        for x, valor in enumerate(linha):
            if valor == caractere:
                return (y, x)
    return None

def mapa_para_grafo(mapa):
    grafo = {}
    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            if mapa[y][x] in ['.', 'E', 'D']:
                vizinhos = []
                for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < len(mapa) and 0 <= nx < len(mapa[0]):
                        if mapa[ny][nx] in ['.', 'E', 'D']:
                            vizinhos.append((ny, nx))
                grafo[(y, x)] = vizinhos
    return grafo

def bfs(grafo, inicio, destino):
    fila = deque()
    fila.append((inicio, [inicio]))
    visitados = set()
    visitados.add(inicio)

    while fila:
        atual, caminho = fila.popleft()
        if atual == destino:
            return caminho
        for viz in grafo.get(atual, []):
            if viz not in visitados:
                visitados.add(viz)
                fila.append((viz, caminho + [viz]))
    return None

def marcar_caminho(mapa, caminho, simbolo):
    for y, x in caminho:
        if mapa[y][x] == '.':
            mapa[y][x] = simbolo

def imprimir_mapa(mapa):
    for linha in mapa:
        print(''.join(linha))

def imprimir_mapa_colorido(mapa):
    for linha in mapa:
        linha_colorida = ''
        for c in linha:
            if c == '*':
                linha_colorida += f'{AZUL}{c}{RESET}'
            elif c == '+':
                linha_colorida += f'{AMARELO}{c}{RESET}'
            elif c == 'E':
                linha_colorida += f'{VERDE}{c}{RESET}'
            elif c == 'D':
                linha_colorida += f'{VERDE}{c}{RESET}'
            elif c == '#':
                linha_colorida += f'{VERMELHO}{c}{RESET}'                
            else:
                linha_colorida += c
        print(linha_colorida)


def main():
    mapa = ler_mapa('mapa.txt')
    entrada = encontrar_posicao(mapa, 'E')
    destino = encontrar_posicao(mapa, 'D')

    grafo = mapa_para_grafo(mapa)
    caminho_ida = bfs(grafo, entrada, destino)

    if not caminho_ida:
        print("Caminho até o destino não encontrado.")
        return

    marcar_caminho(mapa, caminho_ida[1:-1], '*')  # Marca ida
    caminho_volta = list(reversed(caminho_ida))
    marcar_caminho(mapa, caminho_volta[1:-1], '+')  # Marca volta

    print("Mapa com caminho de ida (*) e volta (+):\n")
    #imprimir_mapa(mapa)
    imprimir_mapa_colorido(mapa)

if __name__ == '__main__':
    main()