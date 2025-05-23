from database_conection import banco_de_dados

cursor = banco_de_dados[1]

def adicionar_produtos(name, price, quantity):
    cursor.execute(f'''
                INSERT INTO products (name, price, quantity) 
                VALUES ('{name}', {price}, {quantity})''')
    banco_de_dados[0].commit()

def retirar_produtos(name):
    cursor.execute(f'''
                DELETE FROM products WHERE products.name = '{name}'
                ''')
    banco_de_dados[0].commit()
        
def vender_item():
    print('Funcao em desenvolvimento')

def alterar_estoque(id, acao, valor):
    '''
    alterar o banco de dados do estoque de acordo com os parametros
    acao: 'name' para alterar nome, 'price' para alterar preço e 'quantity' para alterar quantidade
    '''
    cursor.execute(f"UPDATE products SET {acao} = %s WHERE id = %s ", (valor, id))
    banco_de_dados[0].commit()

def limpar_estoque():
    cursor.execute(f'DELETE FROM products')
    banco_de_dados[0].commit()
