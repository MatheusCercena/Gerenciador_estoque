from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget

class MenuVertical(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        btn_adicionar = QPushButton('Adicionar produtos no estoque')
        btn_retirar = QPushButton('Retirar produtos do estoque')
        btn_alterar = QPushButton('Alterar produtos em estoque')
        btn_vender = QPushButton('Vender item (e dar desconto)')
        btn_lista = QPushButton('Mostrar itens')
        btn_estatisticas = QPushButton('Mostrar valor total em estoque')
        btn_exportar = QPushButton('Exportar como planilha (csv)')
        btn_sair = QPushButton('Sair')

        layout.addWidget(btn_adicionar)
        layout.addWidget(btn_retirar)
        layout.addWidget(btn_alterar)
        layout.addWidget(btn_vender)
        layout.addWidget(btn_lista)
        layout.addWidget(btn_estatisticas)
        layout.addWidget(btn_exportar)
        layout.addWidget(btn_sair)

        self.setLayout(layout)

