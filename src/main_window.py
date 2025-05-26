from utils.database_system import criar_banco #inicia o banco de dados, importar este e executar OBRIGATORIAMENTE antes dos outros modulos

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QSize

criar_banco()

from UI.widgets.connection_indicator import IndicadorConexao
from UI.widgets.menu import MenuVertical
from UI.widgets.table import TabelaEstoque

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Só Estoque')
        
        #criar o cabeçalho

        header = QLabel('Bem Vindo ao Só Estoque - O Estoque Descomplicado Para o Seu Negócio.')
        header.setStyleSheet("Background-Color: #443B93; font-size: 20px; font-family: Cambria Math;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setFixedHeight(80)

        #cria as instancias/objetos dos widgets

        indicador_conexao = IndicadorConexao()
        menu = MenuVertical()
        menu.setMaximumWidth(600)
        tabela = TabelaEstoque()

        #adiciona os wigets no main

        main = QGridLayout()#linha inicial, coluna inicial, quantas linhas, quantas colunas
        main.addWidget(menu, 0, 0, 2, 1, Qt.AlignmentFlag.AlignLeft)
        main.addWidget(tabela, 0, 1)
        main.addWidget(indicador_conexao, 1, 1, Qt.AlignmentFlag.AlignLeft)

        main.setColumnStretch(0, 4)
        main.setColumnStretch(1, 6)
        main.setRowStretch(0, 85)
        main.setRowStretch(1, 15)

        main.setHorizontalSpacing(100)

        #definindo layout da  janela e colocando na tela

        window = QWidget()

        window_layout = QVBoxLayout()
        window_layout.addWidget(header)
        window_layout.addLayout(main)

        window.setLayout(window_layout)
        self.setCentralWidget(window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

# Definir fatores de alongamento 
# grid.setColumnStretch(0, 1) # Coluna 0 tem stretch 1
# grid.setColumnStretch(1, 2) # Coluna 1 tem stretch 2 (vai ocupar o dobro do espaço da coluna 0)
# grid.setRowStretch(0, 1) # Linha 0 tem stretch 1
# grid.setRowStretch(1, 3) # Linha 1 tem stretch 3 (vai ocupar o triplo do espaço da linha 0)
# grid.setRowStretch(2, 1) # Linha 2 tem stretch 1

# grid.setSpacing(spacing): Define o espaçamento horizontal e vertical entre as células em px.
# grid.setHorizontalSpacing(spacing): Define o espaçamento horizontal entre as células em px.
# grid.setVerticalSpacing(spacing): Define o espaçamento vertical entre as células em px.

# grid.setRowMinimumHeight(row, minHeight): Define a altura mínima da row.
# grid.setColumnMinimumWidth(column, minWidth): Define a largura mínima da column.
 
# widget.setFixedSize(width, height): Define um tamanho fixo para o widget. O widget não crescerá ou encolherá. Isso pode causar problemas se o espaço disponível for menor que o tamanho fixo.
# widget.setMinimumSize(width, height): Define o tamanho mínimo do widget. Ele pode crescer, mas não ficará menor que este tamanho.
# widget.setMaximumSize(width, height): Define o tamanho máximo do widget. Ele pode encolher, mas não ficará maior que este tamanho.
# widget.setSizePolicy(horizontal_policy, vertical_policy): Esta é uma das propriedades mais poderosas. Define como o widget deve se comportar quando o layout tem espaço disponível para expandir ou contrair. As políticas comuns são:

#     QSizePolicy.Fixed: O widget tem um tamanho fixo.
#     QSizePolicy.Minimum: O widget pode crescer, mas não encolher abaixo do seu tamanho mínimo (minimumSizeHint()).
#     QSizePolicy.Maximum: O widget pode encolher, mas não crescer acima do seu tamanho máximo (maximumSizeHint()).
#     QSizePolicy.Preferred: O widget prefere seu tamanho (sizeHint()), mas pode crescer ou encolher.
#     QSizePolicy.Expanding: O widget prefere seu tamanho, mas se expandirá para preencher o espaço disponível.
#     QSizePolicy.MinimumExpanding: O widget se expandirá, mas respeitará seu tamanho mínimo.
#     QSizePolicy.Ignored: O widget ignorará as sugestões de tamanho e se expandirá o máximo possível.
