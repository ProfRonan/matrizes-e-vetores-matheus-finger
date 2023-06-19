"""Módulo com as funções de manipulação de matrizes."""
from tipos import Escalar, Matriz

# py -m pip install --user black isort pylist


def soma(x: Matriz, y: Matriz) -> Matriz | None:
    """Soma duas matrizes"""
    # TODO: implementar
    # a soma de duas matrizes [[1, 2, 4], [2, 3, 4]] + [[2, 3, 4], [1, 2, 4]] é [[3, 5, 8], [3, 5, 8]]
    # a soma só pode ser realizada se as matrizes tem a mesma quantidade de linhas e colunas.
    # caso contrário, deve retornar None
    if len(x) == 0 or len(y) == 0:
        if len(x) == 0 and len(y) == 0:
            return []
        return None
    if len(x) == len(y) and len(x[0]) == len(y[0]):
        m_soma = []
        for i, _ in enumerate(x):
            lista_soma = []
            for j, _ in enumerate(x[0]):
                lista_soma.append(x[i][j] + y[i][j])
            m_soma.append(lista_soma)
        return m_soma
    return None


def multiplicacao_por_escalar(matriz: Matriz, escalar: Escalar) -> Matriz:
    """Multiplica uma matriz por um escalar"""
    # TODO: implementar
    # a multiplicacao de uma matriz [[1, 2, 4], [2, 3, 4]] por um escalar 2 é [[2, 4, 8], [4, 6, 8]]
    mult = []
    for _, linha in enumerate(matriz):
        lista_mult = []
        for _, valor in enumerate(linha):
            lista_mult.append(valor * escalar)
        mult.append(lista_mult)
    return mult


def multiplicacao(x: Matriz, y: Matriz) -> Matriz | None:
    """Multiplica duas matrizes"""
    # TODO: implementar
    # a multiplicacao de duas matrizes [[1, 2, 4], [2, 3, 4]] por [[2, 3, 4], [1, 2, 4]] é [[10, 17, 28], [12, 20, 32]]
    # a multiplicacao só pode ser realizada se a quantidade de colunas da primeira matriz é igual a quantidade de linhas da segunda matriz.
    # caso contrário, deve retornar None
    mult = []
    if len(x) == 0 and len(y) == 0:
        return mult
    if len(x[0]) == len(y):
        # percorrendo as linhas da matriz x
        for k, _ in enumerate(x):
            linha_mult = []
            # percorrendo colunas da matrix y
            for l in range(0, len(y[0])):
                soma_mult = 0
                # percorrendo colunas de x e as linhas de y
                for m, _ in enumerate(y):
                    soma_mult += x[k][m] * y[m][l]
                linha_mult.append(soma_mult)
            mult.append(linha_mult)
        return mult
    return None


def norma(x: Matriz) -> float:
    """Calcula a norma de uma matriz"""
    # TODO: implementar
    # a norma de uma matriz [[1, 2, 4], [2, 3, 4]] é 6.928203230275509
    # ela consiste em calcular a raiz quadrada da soma dos quadrados dos elementos da matriz
    # caso a matriz esteja vazia deve-se retornar 0
    norma_result = 0
    for _, linha in enumerate(x):
        for _, valor in enumerate(linha):
            norma_result += valor**2
    return norma_result**0.5


def e_simetrica(x: Matriz) -> bool:
    """Verifica se uma matriz é simétrica"""
    # TODO: implementar
    # uma matriz é simétrica se ela é quadrada e se ela é igual a sua transposta
    # a transposta de uma matriz é a matriz que tem as linhas da matriz original como colunas e as colunas da matriz original como linhas
    if len(x) == 0:
        return True
    if len(x) == len(x[0]):
        transposta_sim = []
        for coluna, _ in enumerate(x[0]):
            linha_trans = []
            for linha, _ in enumerate(x):
                linha_trans.append(x[linha][coluna])
            transposta_sim.append(linha_trans)
        if x == transposta_sim:
            return True
    return False


def transposta(x: Matriz) -> Matriz:
    """Calcula a transposta de uma matriz"""
    # TODO: implementar
    # a transposta de uma matriz [[1, 2, 4], [2, 3, 4]] é [[1, 2], [2, 3], [4, 4]]
    if len(x) == 0:
        return []
    m_transposta = []
    for coluna, _ in enumerate(x[0]):
        linha_trans = []
        for linha, _ in enumerate(x):
            linha_trans.append(x[linha][coluna])
        m_transposta.append(linha_trans)
    return m_transposta
