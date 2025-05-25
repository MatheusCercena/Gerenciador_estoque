from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from widgets.connection_indicator import indicador_conexao

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Só Estoque')
        self.setCentralWidget(indicador_conexao)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
