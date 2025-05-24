''''
Principais funções responsáveis por manipular o banco de dados.
'''

from src.utils.database_system import banco_de_dados
from src.utils.buscar_dados import propriedades_produto
from src.data.dumps import armazenar_registro_venda

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
        

def vender_item(id, preco, desconto, quantidade_venda):
    prod_data = propriedades_produto(id)
    quantidade_em_estoque = prod_data['quantidade']
    if quantidade_venda > quantidade_em_estoque:
        return print('Não há quantidade suficiente em estoque')    
    quantidade_restante = quantidade_em_estoque - quantidade_venda
    valor = (1-(desconto/100)) * float(preco)
    cursor.execute('UPDATE products SET price = %s WHERE id = %s', (valor, id))
    cursor.execute('UPDATE products SET quantity = %s WHERE id = %s', (quantidade_restante, id))
    banco_de_dados[0].commit()

    armazenar_registro_venda(prod_data['nome'], id, preco, desconto, valor, quantidade_venda, quantidade_restante)


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

    