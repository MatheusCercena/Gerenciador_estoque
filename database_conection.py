from database_system import conectar_ao_servidor

HOST = 'localhost'
USER = 'root'
PASSWORD = '1234' # Sua senha do MySQL
DATABASE = 'sale'

banco_de_dados = conectar_ao_servidor(HOST, USER, PASSWORD, DATABASE)
