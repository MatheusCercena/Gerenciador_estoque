from database_conection import banco_de_dados

cursor = banco_de_dados[1]

def solicitar_produto(frase: str):
    produtos_disponiveis = []
    [produtos_disponiveis.append(linha[1]) for linha in listar_itens(banco_de_dados)]

    while True:
        produto = input(frase)
        if produto in produtos_disponiveis:
            return produto
        else:
            print('Produto inexistente. Asseguresse de digitar o nome exato que o produto foi cadastrado no estoque.')

def pegar_ID(name: str):
    '''
    retorna o valor <int> de 'id' do produto no banco de dados
    name: nome do produto a retornar o id
    '''
    cursor.execute(f'SELECT id FROM products WHERE name = %s ', (name,))
    resultado = cursor.fetchone()

    return resultado[0]

def propriedades_produto(id):
    '''
    Retona um dicionario com nome, preço e quantidade de um produto
    name: nome do produto
    '''
    cursor.execute(f'SELECT name, price, quantity FROM products WHERE id = %s ', (id,))
    resultado = cursor.fetchone()
    _name = resultado[0]
    price = resultado[1]
    quantidade = resultado[2]

    return {'nome': _name, 'preco' : price, 'quantidade' : quantidade}

def exibir_lista_de_items():
    '''
    Imprime uma lista formatada com os itens da tabela do banco de dados, usando listar_itens() para buscar os dados
    '''
    lista_de_itens = listar_itens()
    print('')
    print('LISTA DE PRODUTOS:')
    print('') 
    for linha in lista_de_itens:
        linha_exibida = f'ID: {linha[0]: >10} | Produto: {linha[1]: >25} | Valor: {linha[2]: >10} R$ | Qntd em estoque: {linha[3]: >10}'
        print(linha_exibida)
        print('- '*int(len(linha_exibida)/2+1))
        print('')

def listar_itens():
    '''
    retorna uma lista <type: list>, em que cada item da lista é outra lista contendo os valores das dados de cada item no estoque, conforme a ordem em que as colunas aparecem no banco de dados.
    '''

    cursor.execute('SELECT * FROM products')
    lista = []
    for linha in cursor.fetchall():
        linha_exibida = [linha[0], linha[1], linha[2], linha[3]]
        lista.append(linha_exibida)

    return lista

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

def solicitar_opc_num(opcoes: list):
    opcao = None
    while opcao not in opcoes:
        opcao = input('Digite o número da opção desejada: ' )
        try:
            opcao = int(opcao)
            return opcao
        except:
            opcao = input('Digite o número da opção desejada: ' )
