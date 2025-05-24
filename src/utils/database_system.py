'''
Funcões principais referente a conexão ao servidor MySQL
'''

from mysql.connector import connect

def conectar_ao_servidor(host, user, password, database):
    banco_de_dados = connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if banco_de_dados.is_connected():
        print(f'Conectado ao banco de dados: {database}.')

    cursor = banco_de_dados.cursor()
    return banco_de_dados, cursor

def fechar_banco_dados(banco_de_dados):
    banco_de_dados[0].close()
    banco_de_dados[1].close()

HOST = 'localhost'
USER = 'root'
PASSWORD = '1234'
DATABASE = 'sale'

banco_de_dados = conectar_ao_servidor(HOST, USER, PASSWORD, DATABASE)
