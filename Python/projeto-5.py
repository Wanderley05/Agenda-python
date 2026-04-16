# determinar quantas figurinhas carimbadas faltam para completar o álbum
# A primeira linha contém três números inteiros N, C e M indicando respectivamente o número de
# figurinhas (e espaços) do álbum, o número de figurinhas carimbadas do álbum e o número de
# figurinhas já compradas. A segunda linha contém C números inteiros distintos Xi indicando as
# figurinhas carimbadas do álbum. A terceira linha contém M números inteiros Yi indicando as
# figurinhas já compradas.
# Saída
# Seu programa deve produzir uma única linha, contendo um inteiro, o número de figurinhas
# carimbadas que faltam para completar o álbum.


N, C, M = 10, 2, 5
carimbadas = {4, 7}
compradas = {7, 1, 2, 8, 3}

try:  # O bloco try é usado para capturar exceções que podem ocorrer durante a execução do código. Se uma exceção ocorrer, o programa irá pular para o bloco except e executar o código lá.
    # map é uma função que aplica uma função a cada item de um iterável (como uma lista) e retorna um iterador. No caso, estamos usando map para converter as entradas de string para inteiros.
    N, C, M = map(int, input().split())
    # set é uma coleção de elementos únicos e não ordenados. No caso, estamos usando set para armazenar as figurinhas carimbadas, pois não queremos duplicatas.
    carimbadas = set(map(int, input().split()))
    compradas = set(map(int, input().split()))
# O bloco except é usado para capturar a exceção ValueError, que ocorre quando a conversão de string para inteiro falha (por exemplo, se o usuário digitar algo que não seja um número). Se isso acontecer, o programa irá imprimir uma mensagem de erro e usar os valores de exemplo definidos anteriormente.
except ValueError:
    print("valores de saida invalidos: ")

# o operador de subtração (-) em conjuntos retorna um novo conjunto com os elementos que estão no primeiro conjunto, mas não no segundo.
faltando = carimbadas - compradas
# len é uma função que retorna o número de itens em um objeto. No caso, estamos usando len para contar quantas figurinhas carimbadas faltam para completar o álbum.
print(len(faltando))
# sorted é uma função que retorna uma nova lista ordenada a partir dos elementos de um iterável. No caso, estamos usando sorted para ordenar as figurinhas carimbadas faltando antes de imprimi-las.
print("Figurinhas carimbadas faltando:", sorted(list(faltando)))
# Verifica se os valores de C e M estão dentro do intervalo permitido (1 a N). Se não estiverem, imprime uma mensagem de erro e encerra o programa.
if not (1 <= C <= N and 1 <= M <= N):
    print("Entrada inválida")
    exit()
