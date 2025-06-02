''''
Principais funções responsáveis por manipular o banco de dados.
'''

from db.db import get_connection
from estoque.buscar_dados import propriedades_produto
from data.exports import armazenar_registro_venda

def adicionar_produtos(name, price, quantity):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute(f'''
                INSERT INTO products (name, price, quantity) 
                VALUES ('{name}', {price}, {quantity})''')
    conexao.commit()
    cursor.close()
    conexao.close()


def retirar_produtos(name):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute(f'''
                DELETE FROM products WHERE products.name = '{name}'
                ''')
    conexao.commit()
    
    cursor.close()
    conexao.close()


def vender_item(id, preco, desconto, quantidade_venda):

    conexao = get_connection()
    cursor = conexao.cursor()

    prod_data = propriedades_produto(id)
    quantidade_em_estoque = prod_data['quantidade']
    if quantidade_venda > quantidade_em_estoque:
        return print('Não há quantidade suficiente em estoque')    
    quantidade_restante = quantidade_em_estoque - quantidade_venda
    valor = (1-(desconto/100)) * float(preco)
    cursor.execute('UPDATE products SET price = %s WHERE id = %s', (valor, id))
    cursor.execute('UPDATE products SET quantity = %s WHERE id = %s', (quantidade_restante, id))
    conexao.commit()
    
    cursor.close()
    conexao.close()

    armazenar_registro_venda(prod_data['nome'], id, preco, desconto, valor, quantidade_venda, quantidade_restante)


def alterar_estoque(id, acao, valor):
    '''
    alterar o banco de dados do estoque de acordo com os parametros
    acao: 'name' para alterar nome, 'price' para alterar preço e 'quantity' para alterar quantidade
    '''
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute(f"UPDATE products SET {acao} = %s WHERE id = %s ", (valor, id))
    conexao.commit()

    cursor.close()
    conexao.close()


def limpar_estoque():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute(f'DELETE FROM products')
    conexao.commit()

    cursor.close()
    conexao.close()
