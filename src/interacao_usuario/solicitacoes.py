from utils.buscar_dados import listar_itens

def solicitar_produto(frase: str):
    produtos_disponiveis = []
    [produtos_disponiveis.append(linha[1]) for linha in listar_itens()]

    while True:
        produto = input(frase)
        if produto in produtos_disponiveis:
            return produto
        else:
            print('Produto inexistente. Asseguresse de digitar o nome exato que o produto foi cadastrado no estoque.')


def solicitar_opcao_numerica(opcoes: list):
    opcao = None
    while opcao not in opcoes or type(opcao) != int:
        opcao = input('Digite o número da opção desejada: ' )
        try:
            opcao = int(opcao)
        except:
            opcao = input('Digite o número da opção desejada: ' )
    return opcao

def validar_float(valor):
    while True:
        try:
            valor = float(valor)
            return valor
        except:
            valor = input('Erro digite um número: ' )

def validar_int(valor):
    while True:
        try:
            valor = int(valor)
            return valor
        except:
            valor = input('Erro digite um número inteiro: ' )


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
