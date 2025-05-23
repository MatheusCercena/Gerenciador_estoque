

def solicitar_produto(banco_de_dados, frase: str):
    produtos_disponiveis = []
    [produtos_disponiveis.append(linha[1]) for linha in listar_itens(banco_de_dados)]

    while True:
        produto = input(frase)
        if produto in produtos_disponiveis:
            return produto
        else:
            print('Produto inexistente. Asseguresse de digitar o nome exato que o produto foi cadastrado no estoque.')

def pegar_ID(banco_de_dados, name: str):
    cursor = banco_de_dados[1]
    cursor.execute(f'SELECT id FROM products WHERE name = %s ', (name,))
    resultado = cursor.fetchone()
    return resultado[0]

def propriedades_produto(banco_de_dados, id: str):
    '''
    Retona um dicionario com nome, preço e quantidade de um produto
    name: nome do produto
    '''
    cursor = banco_de_dados[1]
    cursor.execute(f'SELECT name, price, quantity FROM products WHERE id = %s ', (id,))
    resultado = cursor.fetchone()
    _name = resultado[0]
    price = resultado[1]
    quantidade = resultado[2]

    return {'nome': _name, 'preco' : price, 'quantidade' : quantidade}


def exibir_lista_de_items(banco_de_dados):


    lista_de_itens = listar_itens(banco_de_dados)
    print('')
    print('LISTA DE PRODUTOS:')
    print('') 
    for linha in lista_de_itens:
        linha_exibida = f'ID: {linha[0]: >10} | Produto: {linha[1]: >25} | Valor: {linha[2]: >10} R$ | Qntd em estoque: {linha[3]: >10}'
        print(linha_exibida)
        print('- '*int(len(linha_exibida)/2+1))
        print('')

def listar_itens(banco_de_dados):
    '''
    retorna uma lista, em que cada item da lista é outra lista contendo os valores das dados de cada item no estoque, conforme a ordem em que as colunas aparecem no banco de dados.
    '''
    cursor = banco_de_dados[1]

    cursor.execute('SELECT * FROM products')
    lista = []
    for linha in cursor.fetchall():
        linha_exibida = [linha[0], linha[1], linha[2], linha[3]]
        lista.append(linha_exibida)
        
    return lista

def valor_em_estoque(banco_de_dados):
    cursor = banco_de_dados[1]
    cursor.execute(f'SELECT SUM(price) FROM products')
    resultado = cursor.fetchone()
    soma = resultado[0]

    return soma
