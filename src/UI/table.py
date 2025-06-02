from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
# from PyQt6.QtSql import QSqlDatabase, QSqlTableModel

from estoque.buscar_dados import listar_itens


class TabelaEstoque(QWidget):
    """
    Um QWidget que exibe uma tabela de banco de dados MySQL usando QTableView e QSqlTableModel.
    """
    def __init__(self):
        super().__init__()

    #     database = QSqlDatabase.addDatabase(("QMYSQL"))
    #     database.setHostName(db_config['host'])
    #     database.setUserName(db_config['user'])
    #     database.setPassword(db_config['password'])
    #     database.setDatabaseName(db_config['database'])

    #     modelo = QSqlTableModel(self, database)
    #     modelo.setTable('sale')
    #     modelo.select()

    #     tabela = QTableView(self)
    #     tabela.setModel(modelo)
    #     tabela.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
    #     tabela.resizeColumnsToContents()
    #     tabela.setSortingEnabled(True)


        tabela = QTableWidget()
        database = listar_itens()
        cabecalho = ['Nome', 'Preço', 'Quantidade']
   
        tabela.setRowCount(len(database))
        tabela.setColumnCount(len(cabecalho))
        tabela.setHorizontalHeaderLabels(cabecalho)

        for l, linha in enumerate(database):
                for coluna, valor in enumerate(linha[1:]):
                    celula = QTableWidgetItem(str(valor))
                    tabela.setItem(l, coluna, celula)
                 
        tabela.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tabela.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        
        layout = QVBoxLayout()
        layout.addWidget(tabela)
        self.setLayout(layout)
