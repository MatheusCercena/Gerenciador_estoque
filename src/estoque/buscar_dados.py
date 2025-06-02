'''
Funções para buscar dados do banco de dados, que podem ser úteis para outras funções.
'''

from db.db import get_connection

def listar_itens():
    '''
    retorna uma lista <type: list>, em que cada item da lista é outra lista contendo os valores das dados de cada item no estoque, conforme a ordem em que as colunas aparecem no banco de dados.
    '''
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM products')
    lista = []
    for linha in cursor.fetchall():
        linha_exibida = [linha[0], linha[1], linha[2], linha[3]]
        lista.append(linha_exibida)

    return lista


def pegar_ID(name: str):
    '''
    retorna o valor <int> de 'id' do produto no banco de dados
    name: nome do produto a retornar o id
    '''
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute(f'SELECT id FROM products WHERE name = %s ', (name,))
    resultado = cursor.fetchone()

    return resultado[0]


def propriedades_produto(id):
    '''
    Retona um dicionario com nome, preço e quantidade de um produto
    name: nome do produto
    '''
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute(f'SELECT name, price, quantity FROM products WHERE id = %s ', (id,))
    resultado = cursor.fetchone()
    _name = resultado[0]
    price = resultado[1]
    quantidade = resultado[2]

    return {'nome': _name, 'preco' : price, 'quantidade' : quantidade}


def valor_em_estoque():
    '''
    Retorna o valor total do banco de dados, multiplicando o valor de cada produto do banco de dados por sua quantidade. 
    '''
    products = listar_itens()
    soma = 0
    for produto in products:
        total_produto = produto[2]*produto[3]
        soma += total_produto

    return soma
