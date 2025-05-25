'''
Dedicado a criação de registros de operacões. Essas funcoes geralmente são chamados por funções de operações em src.
'''

import os
import csv
from datetime import datetime
from random import randint
from utils.buscar_dados import listar_itens


def armazenar_registro_venda(prod_data, id, preco, desconto, valor, quantidade_venda, quantidade_restante):
    num_operacao = randint(10000000, 99999999)
    conteudo_log = f'''
REGISTRO DE VENDA
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
        print(f'Registro da venda armazenado na pasta logs dentro da pasta do programa')
    except:
        print('Erro ao armazenar Registro da venda na pasta logs')

def exportar_csv():
    '''
    Exporta os dados do banco de dados para um arquivo CSV.
    '''
    banco = listar_itens()
    cabecalho = ['ID', 'Nome', 'Preço', 'Quantidade']

    nome_arquivo = f'{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}_Tabela_Estoque.csv'
    dir_base = 'csvs/'

    if not os.path.exists(dir_base):
        os.makedirs(dir_base)
    
    full_path = os.path.join(dir_base, nome_arquivo)

    with open(full_path, 'w', newline='', encoding='utf-8') as arquivo:

        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow(cabecalho)
        escritor_csv.writerows(banco)

        print(f'A listagem de estoque foi exportada com sucesso, na pasta CSV dentro da pasta do programa. \n')

