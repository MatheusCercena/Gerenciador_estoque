Gerenciador de Estoque

Este é um projeto simples de gerenciamento de estoque desenvolvido como parte da disciplina de Programação Estruturada do curso de Ciência da Computação. O programa foi inicialmente concebido para ser executado via terminal, oferecendo funcionalidades básicas para controlar produtos em um estoque, como adição, visualização, atualização e remoção de itens.
Funcionalidades Atuais

    Adicionar Produtos: Permite incluir novos itens ao estoque com informações como nome, preço e quantidade.
    Listar Produtos: Exibe todos os produtos atualmente registrados no estoque.
    Atualizar Produtos: Possibilita a modificação de detalhes de um produto existente.
    Remover Produtos: Permite a exclusão de produtos do estoque.

Requisitos e Configuração

Para que este programa funcione corretamente, é essencial ter um servidor MySQL instalado e em execução. O sistema utiliza um banco de dados MySQL para persistir todas as informações do estoque.
Pré-requisitos

    Python 3.x
    MySQL Server
    Bibliotecas Python:
        mysql-connector-python

Configuração do Banco de Dados

    Crie um banco de dados no seu servidor MySQL. Você pode nomeá-lo como preferir, por exemplo, gerenciador_estoque.

    Crie a tabela products dentro deste banco de dados. A estrutura da tabela deve ser similar a esta:

    CREATE TABLE products (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
price DECIMAL(10, 2) NOT NULL,
quantity INT NOT NULL
);
```

    Atualize as credenciais de conexão no arquivo main.py (ou onde sua conexão com o banco de dados estiver configurada) para corresponder às suas informações de usuário, senha, host e nome do banco de dados MySQL.
    Python

    # Exemplo de conexão (ajuste conforme sua configuração)
    conexao = mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="gerenciador_estoque" # Ou o nome que você deu ao seu banco
    )

Como Executar

    Clone o repositório:
    Bash

git clone https://github.com/MatheusCercena/Gerenciador_estoque.git
cd Gerenciador_estoque

Instale as dependências:
Bash

pip install mysql-connector-python

Execute o programa:
Bash

    python main.py

Próximos Passos (Desenvolvimento Futuro)

Este projeto está em transição para uma interface gráfica do usuário (GUI) utilizando PyQt. O objetivo é transformar a interação via terminal em uma experiência mais intuitiva e visual para o usuário. Acompanhe as atualizações para ver o progresso dessa evolução!


