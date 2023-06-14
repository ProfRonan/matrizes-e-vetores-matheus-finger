"""Módulo com as funções de manipulação de matrizes."""


def soma(x: list[list[float]], y: list[list[float]]) -> list[list[float]] | None:
    """Soma duas matrizes"""
    # TODO: implementar
    # a soma de duas matrizes [[1, 2, 4], [2, 3, 4]] + [[2, 3, 4], [1, 2, 4]] é [[3, 5, 8], [3, 5, 8]]
    # a soma só pode ser realizada se as matrizes tem a mesma quantidade de linhas e colunas.
    # caso contrário, deve retornar None
    if len(x) == len(y) and len(x[0]) == len(y[0]):
        soma = []
        for i in range(0, len(x)):
            lista_soma = []
            for j in range(0, len(x[0])):
                lista_soma.append(x[i][j] + y[i][j])
            soma.append(lista_soma)
        return soma
    else:
        return None


def multiplicação_por_escalar(matriz: list[list[float]], escalar: float) -> list[list[float]]:
    """Multiplica uma matriz por um escalar"""
    # TODO: implementar
    # a multiplicação de uma matriz [[1, 2, 4], [2, 3, 4]] por um escalar 2 é [[2, 4, 8], [4, 6, 8]]
    mult = []
    for i in range(0, len(matriz)):
        lista_mult = []
        for j in range(0, len(matriz[0])):
            lista_mult.append(matriz[i][j] * escalar)
        mult.append(lista_mult)
    return mult


def multiplicação(x: list[list[float]], y: list[list[float]]) -> list[list[float]] | None:
    """Multiplica duas matrizes"""
    # TODO: implementar
    # a multiplicação de duas matrizes [[1, 2, 4], [2, 3, 4]] por [[2, 3, 4], [1, 2, 4]] é [[10, 17, 28], [12, 20, 32]]
    # a multiplicação só pode ser realizada se a quantidade de colunas da primeira matriz é igual a quantidade de linhas da segunda matriz.
    # caso contrário, deve retornar None
    if len(x) == len(y):
        mult = []
        # percorrendo as linhas da matriz x
        for k in range(0, len(x[0])):
            linha_mult = []
            # percorrendo colunas da matrix y
            for l in range(0, len(y)):
                soma = 0
                # percorrendo colunas de x e linhas de y ao mesmo tempo
                for m in range(0, len(y)):
                    soma += x[k][m] * y[m][l]
                linha_mult.append(soma)
            mult.append(linha_mult)
        return mult
    else:
        return None



def norma(x: list[list[float]]) -> float:
    """Calcula a norma de uma matriz"""
    # TODO: implementar
    # a norma de uma matriz [[1, 2, 4], [2, 3, 4]] é 6.928203230275509
    # ela consiste em calcular a raiz quadrada da soma dos quadrados dos elementos da matriz
    # caso a matriz esteja vazia deve-se retornar 0
    norma = 0
    for i in range(0, len(x)):
        for j in range(0, len(x[0])):
            norma += (x[i][j] ** 2)
    return (norma ** 0.5)


def é_simétrica(x: list[list[float]]) -> bool:
    """Verifica se uma matriz é simétrica"""
    # TODO: implementar
    # uma matriz é simétrica se ela é quadrada e se ela é igual a sua transposta
    # a transposta de uma matriz é a matriz que tem as linhas da matriz original como colunas e as colunas da matriz original como linhas


def transposta(x: list[list[float]]) -> list[list[float]]:
    """Calcula a transposta de uma matriz"""
    # TODO: implementar
    # a transposta de uma matriz [[1, 2, 4], [2, 3, 4]] é [[1, 2], [2, 3], [4, 4]]