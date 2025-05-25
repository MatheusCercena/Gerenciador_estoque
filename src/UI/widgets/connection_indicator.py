from PyQt6.QtWidgets import QWidget, QLabel
from utils.exibicoes import definir_verificador_de_conexao

indicador_conexao = QWidget


texto = definir_verificador_de_conexao()

texto_indicador = QLabel(texto)

indicador_conexao.setLayout(texto_indicador)

