from PyQt6.QtWidgets import QLabel
from utils.exibicoes import status_da_conexao

texto = status_da_conexao()

class indicator(QLabel):
    def __init__(self):
        super().__init__(texto)

