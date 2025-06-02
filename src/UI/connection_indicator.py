from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout
from utils.exibicoes import status_da_conexao

texto = status_da_conexao()

class IndicadorConexao(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel(texto)

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)
