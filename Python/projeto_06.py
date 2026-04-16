# A primeira linha da entrada contém um inteiro N indicando o número de botas individuais entregues. Cada
# uma das N linhas seguintes descreve uma bota, contendo um número inteiro M e uma letra L, separados
# por um espaço em branco. M indica o número do tamanho da bota e L indica o pé da bota: L='D' indica que
# a bota é para o pé direito, L='E' indica que a bota é para o pé esquerdo.
# Saída
# Seu programa deve imprimir uma única linha contendo um único número inteiro indicando o número total de
# pares corretos de botas que podem ser formados a partir das N botas entregues.

from collections import defaultdict

# Valores de exemplo para teste
N = 10
botas_quantidade = [
    (38, 'D'),
    (38, 'E'),
    (39, 'D'),
    (39, 'E'),
    (40, 'D'),
    (40, 'E'),
    (38, 'D'),
    (38, 'E'),
    (39, 'D'),
    (39, 'E')
]

try:
    N = int(input())
    botas = []
    for _ in range(N):
        M, L = input().split()
        M = int(M)
        botas.append((M, L))
except (ValueError, EOFError):
    print("Usando valores de exemplo devido a entrada inválida.")
    botas = botas_quantidade

contadores = defaultdict(lambda: {'D': 0, 'E': 0})

for M, L in botas:
    contadores[M][L] += 1

pares = 0
for tamanho in contadores:
    pares += min(contadores[tamanho]['D'], contadores[tamanho]['E'])

print(pares)
