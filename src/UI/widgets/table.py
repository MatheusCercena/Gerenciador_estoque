from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableView
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel

from utils.database_system import HOST, USER, PASSWORD, DATABASE


class TabelaEstoque(QWidget):
    """
    Um QWidget que exibe uma tabela de banco de dados MySQL usando QTableView e QSqlTableModel.
    """
    def __init__(self):
        super().__init__()

        database = QSqlDatabase.addDatabase(("QMYSQL"))
        database.setHostName(HOST)
        database.setUserName(USER)
        database.setPassword(PASSWORD)
        database.setDatabaseName(DATABASE)

        modelo = QSqlTableModel(self, database)
        modelo.setTable('sale')

        tabela = QTableView(self)
        tabela.setModel(modelo)
        tabela.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        tabela.resizeColumnsToContents()
        tabela.setSortingEnabled(True)

        layout = QVBoxLayout()
        layout.addWidget(tabela)
        self.setLayout(layout)
