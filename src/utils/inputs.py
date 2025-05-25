'''
Funçoes para solicitar ou validar inputs do usuário.
'''

from utils.buscar_dados import listar_itens
from utils.cores import RED, RESET

def validar_float(valor):
    while True:
        try:
            valor = float(valor)
            return valor
        except:
            valor = input(f'{RED}[ERRO]{RESET} digite apenas números: ' )

def validar_int(valor):
    while True:
        try:
            valor = int(valor)
            return valor
        except:
            valor = input(f'{RED}[ERRO]{RESET} digite um número inteiro: ' )


def solicitar_produto(frase: str):
    produtos_disponiveis = []
    [produtos_disponiveis.append(linha[1]) for linha in listar_itens()]

    while True:
        produto = input(frase)
        if produto in produtos_disponiveis:
            return produto
        else:
            print(f'{RED}Produto inexistente.{RESET} Asseguresse de digitar o nome exato que o produto foi cadastrado no estoque.')


def solicitar_opcao_numerica(opcoes: list):
    opcao = None
    while opcao not in opcoes or type(opcao) != int:
        opcao = input('Digite o número da opção desejada: ' )
        try:
            opcao = int(opcao)
        except:
            print(f'{RED}O número precisa estar entre {opcoes[0]} e {opcoes[-1]}{RESET}')
            opcao = input('Digite o número da opção desejada: ' )
    return opcao


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
