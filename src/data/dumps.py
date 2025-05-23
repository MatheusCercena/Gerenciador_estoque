import os
from datetime import datetime
from random import randint

def armazenar_registro_venda(prod_data, id, preco, desconto, valor, quantidade_venda, quantidade_restante):
    num_operacao = randint(10000000, 99999999)
    conteudo_log = f'''
Registro de venda
ID operação = {num_operacao}
Data / hora {datetime.now().strftime("%d_%m_%Y_%H_%M_%S")} 
Produto = {prod_data}
ID do produto = {id}
Valor Original = {preco} R$
Desconto [%] = {desconto}
Valor de venda com desconto = {valor} R$
Unidades vendidas = {quantidade_venda} un
Unidades restantes em estoque = {quantidade_restante} un
Valor total da venda = {valor*quantidade_venda} R$
        '''
    nome_do_registro = f'{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}_{num_operacao}.txt'
    dir_base = 'logs/'

    if not os.path.exists(dir_base):
        os.makedirs(dir_base)

    full_path = os.path.join(dir_base, nome_do_registro)
    print(f'3 {full_path}')

    try:
        with open(full_path, 'w', encoding='utf-8') as log:
            log.write(conteudo_log)
        print(f'Registro da venda armazenado em {full_path}')
    except:
        print('Erro ao armazenar Registro da venda na pasta logs')
