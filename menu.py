
from database_system import conectar_ao_servidor, fechar_banco_dados
from alterar_banco import (
adicionar_produtos, 
retirar_produtos,
alterar_estoque,
comprar_item,
vender_item,
limpar_estoque,
)
from buscar_dados import (
solicitar_produto,
pegar_ID,
propriedades_produto,
exibir_lista_de_items,
valor_em_estoque
)





banco_de_dados = conectar_ao_servidor('localhost', 'root', '1234', 'sale')

while True:
    print(f'''
----------------------
Bem vindo:
----------------------
O que deseja fazer?
      
[1] Adicionar produtos no estoque
[2] Retirar produtos do estoque
[3] Alterar produtos em estoque
[4] Comprar item
[5] Vender item (e dar desconto)
[6] Mostrar itens
[7] Mostrar valor total em estoque
[8] Limpar estoque
[9] Exportar como planilha (csv)
[10] Sair
----------------------
''')

    opcoes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    opcao = None
    while opcao not in opcoes:
        opcao = int(input('Digite o número da opção desejada: ' ))
        
    if opcao == 1:
        produto = input('Produto: ')
        valor = input('Valor: ')
        quantidade = input('Quantidade: ')
        adicionar_produtos(banco_de_dados, produto, valor, quantidade)

    elif opcao == 2:
        exibir_lista_de_items(banco_de_dados)
        produto = solicitar_produto(banco_de_dados, 'Qual produto deseja remover? ')

        verificacao = input(f'Você irá remover o produto {produto}, deseja continuar [digite enter para SIM qualquer outra tecla para NÃO]: ')
        if verificacao == '' :
            retirar_produtos(banco_de_dados, produto)
        else:
            continue

    elif opcao == 3:
        exibir_lista_de_items(banco_de_dados)
        produto = solicitar_produto(banco_de_dados, 'Qual produto deseja alterar? ')
        id = pegar_ID(banco_de_dados, produto)
        preco = propriedades_produto(banco_de_dados, id)['preco']
        quantidade = propriedades_produto(banco_de_dados, id)['quantidade']

        res = input(f'''
                    Produto selecionado: 
                    Nome: {produto}| Valor: {preco} R$ | Quantidade: {quantidade}
                    O que deseja alterar?
                    Digite [1] para Nome: 
                    Digite [2] para Preço: 
                    Digite [3] para Quantidade: 

                    ''')
        nova_info = ''
        opt = str('')
        if res == '1':
            opt = 'name'
            nova_info = input(f'Insira o novo nome do produto: ')
        if res == '2':
            opt = 'price'
            nova_info = input(f'Insira o novo preço do produto: ')
        if res == '3':
            opt = 'quantity'
            nova_info = input(f'Insira a nova quantidade do produto: ')
        
        alterar_estoque(banco_de_dados, id, opt, nova_info)

        novo_nome = propriedades_produto(banco_de_dados, id)['nome']
        nova_preco = propriedades_produto(banco_de_dados, id)['preco']
        nova_quantidade = propriedades_produto(banco_de_dados, id)['quantidade']

        print(f'''
              Estoque alterado! 
              O que foi alterado: 
              ANTIGO Nome {produto}| Valor: {preco} R$ | Quantidade: {quantidade}
              NOVO Nome {novo_nome}| Valor: {nova_preco} R$ | Quantidade: {nova_quantidade}
              ''')

    elif opcao == 4:
        comprar_item(banco_de_dados)

    elif opcao == 5:
        vender_item(banco_de_dados)

    elif opcao == 6:
        exibir_lista_de_items(banco_de_dados)
        
    elif opcao == 7:
        print(f'O valor do carrinho é {valor_em_estoque(banco_de_dados)}')

    elif opcao == 8:
        aviso = input('Deseja realmente deletar todos os items do estoque? ')
        confirmação = input('''
                            Deseja realmente deletar todos os items do estoque? 
                            Digite exatamente a frase a abaixo para confirmar \n
                            [Estou ciente de que é uma ação irreverssível]: \n
                            ''')
        if confirmação == 'Estou ciente de que é uma ação irreverssível':
            limpar_estoque(banco_de_dados)
            print('Os items do estoque foram deletados com sucesso')
    elif opcao == 9:
        print('Função em desenvolvimento')
    else:
        fechar_banco_dados(banco_de_dados)
    
    input('Voltar ao menu-principal (digite qualquer tecla): ')