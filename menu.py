from database_conection import banco_de_dados
from database_system import fechar_banco_dados
from alterar_banco import (
adicionar_produtos, 
retirar_produtos,
alterar_estoque,
vender_item,
limpar_estoque
)
from buscar_dados import (
solicitar_produto,
pegar_ID,
propriedades_produto,
exibir_lista_de_items,
valor_em_estoque,
solicitar_opc_num
)

mensagem_menu = f'''
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

confirmação_limpar_estoque = '''
                            Deseja realmente deletar todos os items do estoque? 
                            Digite exatamente a frase a abaixo para confirmar \n
                            [Estou ciente de que é uma ação irreverssível]: \n
                            '''

# Começo do Menu

while True:
    print(mensagem_menu)

    opcoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    opcao = solicitar_opc_num(opcoes)

    if opcao == 1: #Adicionar produtos no estoque
        produto = input('Produto: ')
        valor = input('Valor: ')
        quantidade = input('Quantidade: ')
        adicionar_produtos(produto, valor, quantidade)

    elif opcao == 2: #Retirar produtos do estoque
        exibir_lista_de_items()
        produto = solicitar_produto('Qual produto deseja remover? ')

        verificacao = input(f'Você irá remover o produto {produto}, deseja continuar [digite enter para SIM qualquer outra tecla para NÃO]: ')
        if verificacao == '' :
            retirar_produtos(produto)
        else:
            continue

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
        opcao = solicitar_opc_num(opcoes)

        nova_info = ''
        acao = ''
        if opcao == '1':
            acao = 'name'
            nova_info = input(f'Insira o novo nome do produto: ')
        if opcao == '2':
            acao = 'price'
            nova_info = input(f'Insira o novo preço do produto: ')
        if opcao == '3':
            acao = 'quantity'
            nova_info = input(f'Insira a nova quantidade do produto: ')
        
        alterar_estoque(id, acao, nova_info)
        new_data = propriedades_produto(id)

        print(f'''
              Estoque alterado! 
              O que foi alterado: 
              ANTIGO Nome {prod_data['nome']}| Valor: {prod_data['preco']} R$ | Quantidade: {prod_data['quantidade']}
              NOVO Nome {new_data['nome']}| Valor: {new_data['preco']} R$ | Quantidade: {new_data['quantidade']}
              ''')

    elif opcao == 4: #Vender item
        vender_item()

    elif opcao == 5: #Mostrar itens
        exibir_lista_de_items()
        
    elif opcao == 6: #Mostrar valor total em estoque
        print(f'O valor do carrinho é {valor_em_estoque()}')

    elif opcao == 7: #Limpar estoque
        aviso = input('Deseja realmente deletar todos os items do estoque? ')
        confirmação = input(confirmação_limpar_estoque)
        if confirmação == 'Estou ciente de que é uma ação irreverssível':
            limpar_estoque()
            print('Os items do estoque foram deletados com sucesso')
    elif opcao == 8: #Exportar como planilha (csv)
        print('Função em desenvolvimento')
    else: #Sair
        fechar_banco_dados(banco_de_dados)
    
    input('Voltar ao menu-principal (digite qualquer tecla): ')