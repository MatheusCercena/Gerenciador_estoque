from utils.database_system import criar_banco #inicia o banco de dados, importar este e executar OBRIGATORIAMENTE antes dos outros modulos

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout


criar_banco()

from UI.widgets.connection_indicator import indicator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Só Estoque')

        central_widget = QWidget()
        

        self.indicador_conexao = indicator()

        main_layout = QGridLayout()
        main_layout.addWidget(self.indicador_conexao, 1, 1, 1, 1)
        
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
