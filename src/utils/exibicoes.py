'''
Mensagens padrão que são longas e podem poluir o código, de forma que ficam em um módulo separado
'''

from utils.cores import RED, RESET
from utils.database_system import verificar_conexao, banco_de_dados

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
    verificador_conexao = verificar_conexao(banco_de_dados)
    if verificador_conexao[0] == True:
        print(f'{'\033[32m'}Conectado ao banco de dados: {verificador_conexao[1]}.{'\033[0m'}')
    if verificador_conexao[0] == False:
        print(f'{'\033[31m'}Erro ao conectar ao banco de dados: {verificador_conexao[1]}.{'\033[0m'}')
