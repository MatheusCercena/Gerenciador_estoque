'''
exibe o menu ciclicamente por condição WHILE de acordo com a opção selecionada pelo usuário
'''

from utils.database_system import fechar_banco_dados, banco_de_dados
from utils.alterar_banco import adicionar_produtos, retirar_produtos, alterar_estoque, vender_item, limpar_estoque
from utils.buscar_dados import pegar_ID, propriedades_produto, valor_em_estoque
from interacao_usuario.solicitacoes import solicitar_produto, exibir_lista_de_items, solicitar_opcao_numerica, validar_float, validar_int
from interacao_usuario.mensagens import msg_menu, msg_confirmação_limpar_estoque
from data.dumps import exportar_csv
import sys

while True:
    print(msg_menu)

    opcoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    opcao = solicitar_opcao_numerica(opcoes)

    if opcao == 1: #Adicionar produtos no estoque
        produto = input('Produto: ')
        valor = validar_float(input('Valor: '))
        quantidade = validar_int(input('Quantidade: '))
        adicionar_produtos(produto, valor, quantidade)
        print('Operação realizada com sucesso.')


    elif opcao == 2: #Retirar produtos do estoque
        exibir_lista_de_items()
        produto = solicitar_produto('Qual produto deseja remover? ')
        verificacao = input(f'Você irá remover o produto {produto}, deseja continuar [digite enter para SIM qualquer outra tecla para NÃO]: ')
        if verificacao == '' :
            retirar_produtos(produto)
        print('Operação realizada com sucesso.')

    elif opcao == 3: #Alterar produtos em estoque
        exibir_lista_de_items()
        produto = solicitar_produto('Qual produto deseja alterar? ')
        id = pegar_ID(produto)
        prod_data = propriedades_produto(id)

        print(f'''
              Produto selecionado: 
              Nome: {prod_data['nome']}| Valor: {prod_data['preco']} R$ | Quantidade: {prod_data['quantidade']}
              O que deseja alterar?
              Digite [1] para Nome
              Digite [2] para Preço
              Digite [3] para Quantidade
              Opção desejada: 
              ''')
        
        opcoes = [1, 2, 3]
        opcao = solicitar_opcao_numerica(opcoes)

        nova_info = ''
        acao = ''
        if opcao == 1:
            acao = 'name'
            nova_info = input(f'Insira o novo nome do produto: ')
        if opcao == 2:
            acao = 'price'
            nova_info = input(f'Insira o novo preço do produto: ')
        if opcao == 3:
            acao = 'quantity'
            nova_info = input(f'Insira a nova quantidade do produto: ')
        
        alterar_estoque(id, acao, nova_info)
        new_data = propriedades_produto(id)

        print(f'''
              Estoque alterado! 
              O que foi alterado: 
              ANTIGO Nome: {prod_data['nome']}| Valor: {prod_data['preco']} R$ | Quantidade: {prod_data['quantidade']}
              NOVO Nome: {new_data['nome']}| Valor: {new_data['preco']} R$ | Quantidade: {new_data['quantidade']}
              ''')
        print('Operação realizada com sucesso.')

    elif opcao == 4: #Vender item
        exibir_lista_de_items()
        produto = solicitar_produto('Qual produto deseja vender? ')
        id = pegar_ID(produto)
        prod_data = propriedades_produto(id)
        quantidade_venda = validar_int(input(f'Há {prod_data["quantidade"]} unidades no estoque. Quantas unidades serão vendidas? '))
        desconto = validar_float(input(f'O valor do produto é {prod_data['preco']}. Qual será o desconto? [%] '))

        vender_item(id, prod_data['preco'], desconto, quantidade_venda)
        print('Operação realizada com sucesso.')

    elif opcao == 5: #Mostrar itens
        exibir_lista_de_items()
        
    elif opcao == 6: #Mostrar valor total em estoque
        print(f'O valor do carrinho é {valor_em_estoque()}')

    elif opcao == 7: #Limpar estoque
        confirmação = input(msg_confirmação_limpar_estoque)
        if confirmação == 'Estou ciente de que é uma ação irreverssível':
            limpar_estoque()
            print('Operação realizada com sucesso.')
    elif opcao == 8: #Exportar como planilha (csv)
        exportar_csv()

    else: #Sair
        fechar_banco_dados(banco_de_dados)
        sys.exit(0)
    
    input('Voltar ao menu-principal (digite qualquer tecla): ')