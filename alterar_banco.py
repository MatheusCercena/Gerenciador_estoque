def adicionar_produtos(banco_de_dados, name, price, quantity):
    cursor = banco_de_dados[1]
    cursor.execute(f'''
                INSERT INTO products (name, price, quantity) 
                VALUES ('{name}', {price}, {quantity})''')
    banco_de_dados[0].commit()

def retirar_produtos(banco_de_dados, name):
    cursor = banco_de_dados[1]
    cursor.execute(f'''
                DELETE FROM products WHERE products.name = '{name}'
                ''')
    banco_de_dados[0].commit()
        
def comprar_item():
    print('Funcao em desenvolvimento')

def vender_item():
    print('Funcao em desenvolvimento')

def alterar_estoque(banco_de_dados, id, acao, valor):
    '''
    alterar o banco de dados do estoque de acordo com os parametros
    acao: 'name' para alterar nome, 'price' para alterar preço e 'quantity' para alterar quantidade
    '''
    cursor = banco_de_dados[1]

    cursor.execute(f"UPDATE products SET {acao} = %s WHERE id = %s ", (valor, id))
    banco_de_dados[0].commit()

def limpar_estoque(banco_de_dados):
    cursor = banco_de_dados[1]
    cursor.execute(f'DELETE FROM products')
    banco_de_dados[0].commit()
