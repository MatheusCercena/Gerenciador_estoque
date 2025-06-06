'''
Mensagens padrão que são longas e podem poluir o código, de forma que ficam em um módulo separado
'''

from db.db import get_connection
from utils.cores import RED, RESET
from estoque.buscar_dados import listar_itens

msg_menu = f'''
----------------------
Bem vindo:
----------------------
O que deseja fazer?
      
[1] Adicionar produtos no estoque
[2] Retirar produtos do estoque
[3] Alterar produtos em estoque
[4] Vender item (e dar desconto)
[5] Mostrar itens
[6] Mostrar valor total em estoque
[7] Limpar estoque
[8] Exportar como planilha (csv)
[9] Sair
----------------------
'''


msg_confirmação_limpar_estoque = f'''{RED}
Deseja realmente deletar todos os items do estoque? 
Digite exatamente a frase a abaixo para confirmar \n
Estou ciente de que é uma ação irreverssível: \n
{RESET}'''


def exibir_verificador_de_conexao():
    conexao = get_connection()
    if conexao.is_connected() == True:
        print(f'{'\033[32m'}Conectado ao banco de dados.{'\033[0m'}')
    if conexao.is_connected() == False:
        print(f'{'\033[31m'}Erro ao conectar ao banco de dados.{'\033[0m'}')


def status_da_conexao():
    conexao = get_connection()
    if conexao.is_connected() == True:
        return f'Conectado ao banco de dados.'
    if conexao.is_connected() == False:
        return f'Erro ao conectar ao banco de dados.'


def exibir_lista_de_items():
    '''
    Imprime uma lista formatada com os itens da tabela do banco de dados, usando listar_itens() para buscar os dados
    '''
    lista_de_itens = listar_itens()

    tabela = []
    for linha in lista_de_itens:
        texto = f'ID: {linha[0]: >10} | Produto: {linha[1]: >25} | Valor: {linha[2]: >10} R$ | Qntd em estoque: {linha[3]: >10}'
        tabela.append(texto)
    print('')
    print(f'LISTA DE PRODUTOS:'.center(len(tabela[0])))
    print('') 
    for linha in tabela:
        print(linha)
        print('- '*int(len(tabela[0])/2+1))
    print('')

