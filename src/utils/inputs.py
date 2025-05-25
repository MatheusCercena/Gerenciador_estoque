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

def solicitar_produto(acao: str):
    '''
    acao: indica qual ação será questionada ao usuário, valida se o produto existe
    '''
    produto = input(f'Qual produto deseja {acao}?: ')
    if validar_produto(produto) == True:
        return produto
    else:
        return False


def validar_produto(produto):
    produtos_disponiveis = []
    for linha in listar_itens():
        produtos_disponiveis.append(linha[1])

    while True:
        if produto in produtos_disponiveis:
            return True
        else:
            print(f'{RED}Produto inexistente.{RESET} Asseguresse de digitar o nome exato que o produto foi cadastrado no estoque.')
            return False


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


