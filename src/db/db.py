'''
Funcões principais referente a conexão ao servidor MySQL
'''

from mysql.connector import connect
from config import db_config

def get_connection():

    conexao = connect(**db_config)
    return conexao

